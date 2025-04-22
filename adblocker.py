import os
import platform
import urllib.request
import datetime

class AdBlocker:
    def __init__(self):
        self.os_type = platform.system().lower()
        self.hosts_path = self._get_hosts_path()
        self.ad_domains = [
            'ads.example.com',
            'analytics.example.com',
            'tracker.example.com',
            'advertising.com',
            'doubleclick.net',
            'google-analytics.com',
            'adnxs.com'
        ]

    def _get_hosts_path(self):
        if self.os_type == 'windows':
            return r'C:\Windows\System32\drivers\etc\hosts'
        return '/etc/hosts'

    def backup_hosts(self):
        """Create a backup of the hosts file"""
        backup_path = f'hosts_backup_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
        try:
            with open(self.hosts_path, 'r') as original:
                with open(backup_path, 'w') as backup:
                    backup.write(original.read())
            print(f"Backup created: {backup_path}")
        except PermissionError:
            print("Error: Permission denied. Please run with administrative privileges.")
            exit(1)

    def update_hosts(self):
        """Update hosts file with ad domains"""
        print("Updating hosts file...")
        
        try:
            # Read existing hosts content
            with open(self.hosts_path, 'r') as file:
                hosts_content = file.read()

            # Add ad domains if they don't exist
            new_entries = []
            for domain in self.ad_domains:
                if domain not in hosts_content:
                    new_entries.append(f"127.0.0.1 {domain}")
                    new_entries.append(f"127.0.0.1 www.{domain}")

            if new_entries:
                # Create backup before modifying
                self.backup_hosts()
                
                # Append new entries
                with open(self.hosts_path, 'a') as file:
                    file.write('\n# Ad blocking entries added by Python AdBlocker\n')
                    file.write('\n'.join(new_entries) + '\n')
                
                print("Successfully updated hosts file with ad blocking rules")
            else:
                print("All domains are already blocked")

        except PermissionError:
            print("Error: Permission denied. Please run with administrative privileges.")
            exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            exit(1)

    def remove_blocks(self):
        """Remove ad blocking entries from hosts file"""
        try:
            with open(self.hosts_path, 'r') as file:
                lines = file.readlines()

            # Filter out ad blocking entries
            new_lines = [line for line in lines 
                        if not any(domain in line for domain in self.ad_domains)]

            # Create backup before modifying
            self.backup_hosts()

            # Write filtered content back
            with open(self.hosts_path, 'w') as file:
                file.writelines(new_lines)

            print("Successfully removed ad blocking rules")

        except PermissionError:
            print("Error: Permission denied. Please run with administrative privileges.")
            exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            exit(1)

if __name__ == "__main__":
    print("Simple Python Ad Blocker")
    print("Note: This script requires administrative privileges to modify the hosts file")
    
    blocker = AdBlocker()
    
    while True:
        print("\nOptions:")
        print("1. Enable ad blocking")
        print("2. Disable ad blocking")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            blocker.update_hosts()
        elif choice == '2':
            blocker.remove_blocks()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")