$user = ""
$token = ""
$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $user, $token)))
$headers = @{Authorization=("Basic {0}" -f $base64AuthInfo)}
$repoEndpoint = "https://dev.azure.com/venminder/_apis/git/repositories?api-version=6.1-preview.1"
$repos = Invoke-RestMethod -ErrorVariable restError -Uri $repoEndpoint -Method GET -ContentType "application/json" -Headers $headers
$totalPrCount = 0
$totalPrCountThisYear = 0
$prTable = New-Object -TypeName Hashtable
$take = 1000
$uuid = ""

write-output "Loading..."

foreach ($repo in $repos.value) {
    $skip = 0

    :inner
    do {
        $PrEndpoint = "https://dev.azure.com/venminder/_apis/git/repositories/$($repo.id)/pullrequests?api-version=7.0&searchCriteria.status=completed&searchCriteria.creatorId=$($uuid)&`$top=$($take)&`$skip=$($skip)"
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
                $prCount = 0;

                if ($pr.closedDate -Match "2024") {
                    $totalPrCountThisYear += 1
                }

                if ($prTable[$pr.repository.name]) {
                    $prCount = $prTable[$pr.repository.name];
                }

                $prTable[$pr.repository.name] = $prCount + 1;
            }

            if ($result.Count -lt $take) {
                break inner;
            }
        }
    } while ($true)
}

write-output "Repository Contributions"
$prTable

write-output "`nTotal PRs: $totalPrCount`n";
write-output "`nTotal PRs this year: $totalPrCountThisYear`n";

pause