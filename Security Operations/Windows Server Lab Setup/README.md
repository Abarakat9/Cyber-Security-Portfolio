# Windows Server 2016 Install Lab

A foundational virtualization lab (ITEC 420): building a Windows Server 2016 virtual machine from scratch in VirtualBox.

## What I did

- Installed VirtualBox and created a new virtual machine
- Attached the Windows Server 2016 ISO and configured the VM to boot from it
- Completed the Windows Server install, set credentials, and logged in
- Verified the running server from the command line (`dir`) to confirm a working install

## Why it's here

Standing up a Windows Server VM is the groundwork for nearly every blue-team lab that follows — Active Directory, endpoint telemetry, and the domain-controller vulnerability scanning in the [Vulnerability Management](../../Vulnerability%20Management/) section all assume you can build and run a server in a hypervisor. This lab documents that baseline skill.

## Files

- `Windows Server 2016 Install Lab.docx`
