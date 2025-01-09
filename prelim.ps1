$tools = @("nmap", "ping", "tcpdump")

foreach ($tool in $tools) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        Write-Host "$tool could not be found, please install it."
        exit 1
    }
}