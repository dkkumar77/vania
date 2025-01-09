$tools = @(
    @{ Name = "nmap"; InstallCommand = "winget install -e --id Nmap.Nmap" },
    @{ Name = "tcpdump"; InstallCommand = "winget install -e --id WiresharkFoundation.Wireshark" }, 
    @{ Name = "ping"; InstallCommand = "Built-in"; Message = "Ping is a built-in Windows tool." }

)

foreach ($tool in $tools) {
    $name = $tool.Name
    $installCommand = $tool.InstallCommand
    $message = $tool.Message

    if (-not (Get-Command $name -ErrorAction SilentlyContinue)) {
        if ($message) {
            Write-Host "$name could not be found. $message"
        } elseif ($installCommand) {
            Write-Host "$name could not be found. Attempting to install..."
            try {
                Invoke-Expression $installCommand
                Write-Host "$name installed successfully."
            } catch {
                Write-Host "Failed to install $name. Please install it manually."
            }
        }
    } else {
        Write-Host "$name is already installed."
    }
}





