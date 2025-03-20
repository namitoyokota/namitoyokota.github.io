$user = ""
$token = ""
$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $user, $token)))
$headers = @{Authorization=("Basic {0}" -f $base64AuthInfo)}
$repoEndpoint = "https://dev.azure.com/venminder/_apis/git/repositories?api-version=6.1-preview.1"
$repos = Invoke-RestMethod -ErrorVariable restError -Uri $repoEndpoint -Method GET -ContentType "application/json" -Headers $headers
$totalCommitCount = 0
$take = 1000
$author = "Namito Yokota"

$addCount = 0;
$editCount = 0;
$deleteCount = 0;

write-output "Loading..."

$start = [DateTime]"12/05/2022";
$today = Get-Date

$index = 0
$commitTable = New-Object -TypeName Hashtable
While ($start -lt $today)
{
    $commitTable[$start.ToShortDateString()] = 0;
    $start = $start.AddDays(1);
    $index++;
}

foreach ($repo in $repos.value) {
    $skip = 0

    :inner
    do {
        $CommitEndpoint = "https://dev.azure.com/venminder/_apis/git/repositories/$($repo.id)/commits?api-version=7.0&searchCriteria.author=$($author)&`$top=$($take)&`$skip=$($skip)"
        $skip += $take

        try {
            $result = Invoke-RestMethod -ErrorVariable restError -Uri $CommitEndpoint -Method GET -ContentType "application/json" -Headers $headers -ErrorAction SilentlyContinue
        }
        catch {
            "Unable to get commit count for " + $repo.name
            break inner;
        }

        if (!$restError) {
            $totalCommitCount += $result.Count

            foreach ($commit in $result.value) {
                $addCount = $addCount + $commit.changeCounts.Add;
                $editCount = $editCount + $commit.changeCounts.Edit;
                $deleteCount = $deleteCount + $commit.changeCounts.Delete;

                $commitCount = 0;
                $commitCount = $commitTable[(Get-Date $commit.committer.date).ToShortDateString()];
                $commitTable[(Get-Date $commit.committer.date).ToShortDateString()] = $commitCount + 1;
            }

            if ($result.Count -lt $take) {
                break inner;
            }
        }
    } while ($true)
}

write-output "`nTotal Commits: $totalCommitCount`n";
write-output "Files Added: $addCount";
write-output "Files Edited: $editCount";
write-output "Files Deleted: $deleteCount";

$commitTable.GetEnumerator() | Sort-Object { $_."Name" -as [datetime] } | Select-Object -Property @{N='Date';E={$_.Key}}, @{N='Count';E={$_.Value}} | Export-Csv -NoTypeInformation -Path "./Commits-$(get-date -f yyyy-MM-dd).csv"

pause