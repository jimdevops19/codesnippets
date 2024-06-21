
# Creating a Linode with Shared CPU and Adding an SSH Key

## Step 1: Create a Linode Account

1. Visit [Linode's website](https://www.linode.com) and sign up for an account if you don't already have one.
2. Log in to your Linode account.

## Step 2: Create a Linode with a Shared CPU Plan

1. Once logged in, click on the "Create" button in the top right corner.
2. Select "Linode" from the dropdown menu.

### Configuration

3. **Choose a Distribution**: Select the operating system you want to use (e.g., Ubuntu 22.04 LTS).
4. **Region**: Choose the data center closest to you or your users.
5. **Linode Plan**: Under "Shared CPU," select the $5/month plan (Nanode 1GB).

### Setting Up Your Linode

6. **Label**: Give your Linode a name.
7. **Root Password**: Set a strong root password. You'll use this to log in initially if you don’t use an SSH key.

## Step 3: Generate an SSH Key

SSH keys are a more secure way of logging into a server with SSH than using a password alone.

### On Linux/macOS

1. Open a terminal on your local machine.
2. Generate an SSH key pair using `ssh-keygen`.

    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

3. You'll be prompted to enter a file in which to save the key. Press Enter to accept the default location.

    ```plaintext
    Enter file in which to save the key (/home/your_user/.ssh/id_rsa):
    ```

4. Next, you'll be prompted to enter a passphrase. It's optional but recommended for added security. If you enter a passphrase, you’ll need to enter it every time you use the key.

    ```plaintext
    Enter passphrase (empty for no passphrase):
    ```

    Confirm the passphrase by entering it again.

5. Your public key will be saved to the file `/home/your_user/.ssh/id_rsa.pub`, and your private key will be saved to `/home/your_user/.ssh/id_rsa`.

### On Windows 11

1. Open PowerShell.
2. Generate an SSH key pair using `ssh-keygen`.

    ```powershell
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

3. You'll be prompted to enter a file in which to save the key. Press Enter to accept the default location.

    ```plaintext
    Enter file in which to save the key (C:\Users\your_user\.ssh\id_rsa):
    ```

4. Next, you'll be prompted to enter a passphrase. It's optional but recommended for added security. If you enter a passphrase, you’ll need to enter it every time you use the key.

    ```plaintext
    Enter passphrase (empty for no passphrase):
    ```

    Confirm the passphrase by entering it again.

5. Your public key will be saved to the file `C:\Users\your_user\.ssh\id_rsa.pub`, and your private key will be saved to `C:\Users\your_user\.ssh\id_rsa`.

## Step 4: Add Your SSH Key to the Linode

1. Go back to the Linode creation page.
2. In the "Add SSH Key" field, paste the contents of your `id_rsa.pub` file. You can display the contents using the following command in your terminal or PowerShell:

    ```bash
    cat ~/.ssh/id_rsa.pub
    ```

    (Windows 11 equivalent in PowerShell):

    ```powershell
    type $env:USERPROFILE\.ssh\id_rsa.pub
    ```

3. Copy the output and paste it into the "Add SSH Key" field.

## Step 5: Complete the Linode Creation

1. Review all your settings and click the "Create" button at the bottom of the page.
2. Linode will start provisioning your server. This may take a few minutes.

## Step 6: Connect to Your Linode Using SSH

1. Once your Linode is running, find its IP address on the Linode Dashboard.
2. Open a terminal on your local machine and connect to your Linode using SSH:

    ```bash
    ssh -i ~/.ssh/id_rsa your_username@your_linode_ip
    ```

    (Windows 11 equivalent in PowerShell):

    ```powershell
    ssh -i $env:USERPROFILE\.ssh\id_rsa your_username@your_linode_ip
    ```

3. If you added a passphrase to your SSH key, you'll be prompted to enter it.

## Additional Tips

- **Security Updates**: After logging in, it's good practice to update your system.

    ```bash
    apt update && apt upgrade -y
    ```

- **Disable root login**: Disabling root login is important for security reasons.
  - You can do this by turning on `PermitRootLogin no` in the /etc/ssh/sshd_config file and restart the SSH service

Following these steps will help you create a Linode with a shared CPU plan and securely connect to it using SSH keys.

