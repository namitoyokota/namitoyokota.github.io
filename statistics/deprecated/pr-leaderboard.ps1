$user = ""
$token = ""
$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $user, $token)))
$headers = @{Authorization=("Basic {0}" -f $base64AuthInfo)}
$repoEndpoint = "https://dev.azure.com/venminder/_apis/git/repositories?api-version=6.1-preview.1"
$repos = Invoke-RestMethod -ErrorVariable restError -Uri $repoEndpoint -Method GET -ContentType "application/json" -Headers $headers
$prCounts = New-Object -TypeName Hashtable
$totalPrCount = 0
$take = 1000

write-output "Loading..."

foreach ($repo in $repos.value) {
    write-output $repo.name
    $skip = 0

    :inner
    do {
        $PrEndpoint = "https://dev.azure.com/venminder/_apis/git/repositories/$($repo.id)/pullrequests?api-version=7.0&searchCriteria.status=completed&`$top=$($take)&`$skip=$($skip)"
        $skip += $take

        try {
            $result = Invoke-RestMethod -ErrorVariable restError -Uri $PrEndpoint -Method GET -ContentType "application/json" -Headers $headers -ErrorAction SilentlyContinue
        }
        catch {
            "Unable to get PR count for " + $repo.name
            break inner;
        }

        if (!$restError) {
            $totalPrCount += $result.Count

            foreach ($pr in $result.value) {
                $prCount = 0

                if ($prCounts[$pr.createdBy.uniqueName]) {
                    $prCount = $prCounts[$pr.createdBy.uniqueName]

                    if ($pr.createdBy.uniqueName -eq $user) {
                        write-output $pr.createdBy
                    }
                }

                $prCounts[$pr.createdBy.uniqueName] = $prCount + 1
            }

            if ($result.Count -lt $take) {
                break inner;
            }
        }
    } while ($true)
}

write-output "PR Leaderboards"
$prCounts.GetEnumerator() | Sort Value -Descending

write-output "`nTotal PRs: $totalPrCount";

pause