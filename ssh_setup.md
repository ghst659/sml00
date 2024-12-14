# Adding Your Computer's SSH Key to Your Github Account

This will enable you to `clone` and `push` repositories from
github to/from your computer.

## Generate Public/Private Keypair for Your Computer

Based on
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

0. Log into github.com

1. In a separate terminal, generate Public+Private KeyPair for Your Computer

   ```
   $ ssh-keygen -t rsa -C 'your.name@example.com'
   ```

2. Copy the public-key to your clipboard

   ```
   $ cat ~/.ssh/id_rsa.pub
   # Use terminal's copy-function to copy the string to the clipboard.
   ```

3. On your github.com login page
   1. Click on the account photo upper right
   2. Click Settings
   3. Left sidebar, section "Access", click "SSH and GPG keys"
   4. Under "SSH keys", click "New SSH key"
   5. Give the new Authentication key a title, and paste the public key.
   6. Press "Add SSH key".
