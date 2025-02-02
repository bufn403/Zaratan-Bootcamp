# Connecting to the Zaratan HPC Cluster

Welcome to the Zaratan HPC Cluster. Follow the steps below to access and utilize this powerful computing resource.

## Prerequisites

Before connecting to Zaratan, ensure you have:

1. **Active HPC Account**: Access requires an active HPC account. If you don't have one, request access by following the instructions provided by the university.

2. **Multifactor Authentication (MFA)**: Zaratan uses the campus DUO MFA system. Ensure your DUO MFA is set up and functioning.

3. **SSH Client**: macOS includes a built-in SSH client accessible via the Terminal application.

## Connecting to Zaratan

1. **Connect to the Campus VPN**:
   - Connecting through the campus VPN, which requires MFA, simplifies the login process. If you're on the VPN, SSH connections to Zaratan will not prompt you for additional MFA; you'll only need to enter your password.

2. **Open Terminal**:
   - Launch the Terminal application on your Mac.

3. **Initiate SSH Connection**:
   - Use the SSH command to connect to Zaratan's login node. Replace `your_directory_id` with your UMD directory ID:

     ```bash
     ssh your_directory_id@login.zaratan.umd.edu
     ```

   - If you're not connected to the campus VPN, after entering your password, you'll be prompted to complete the MFA process.

## Transferring Files

To transfer files between your Mac and Zaratan:

- **Using `scp` Command**:
  - Open Terminal and use the `scp` command. For example, to copy a file from your Mac to Zaratan:

    ```bash
    scp /path/to/local/file your_directory_id@login.zaratan.umd.edu:/path/to/remote/directory
    ```

  - To copy a file from Zaratan to your Mac:

    ```bash
    scp your_directory_id@login.zaratan.umd.edu:/path/to/remote/file /path/to/local/directory
    ```

- **Using Cyberduck**:
  - Download and install [Cyberduck](https://cyberduck.io/).
  - Open Cyberduck and click "Open Connection."
  - Select "SFTP (SSH File Transfer Protocol)" from the dropdown.
  - Enter `login.zaratan.umd.edu` as the server and your UMD directory ID as the username.
  - Click "Connect" and enter your password when prompted.

## Important Considerations

- **Avoid Running Intensive Processes on Login Nodes**: The login nodes are intended for tasks like submitting and monitoring jobs, compiling code, and transferring files. Do not run computationally intensive processes on these nodes, as it violates policy and can disrupt other users. Such processes will be terminated without warning, and repeated offenses may lead to suspension of your cluster access privileges.

- **Data Management**:
  - **Home Directory**: Use for storing scripts, source codes, and important data. This space is backed up regularly.
  - **Scratch Directory**: Use the `/scratch` directory for running simulations and storing temporary data. Ensure you back up important data, as scratch storage is not backed up and is purged periodically.

## Additional Resources

- **HPC Documentation**: [https://hpcc.umd.edu/hpcc/help/basics.html](https://hpcc.umd.edu/hpcc/help/basics.html)
- **HPC Support**: [https://hpcc.umd.edu/hpcc/help/](https://hpcc.umd.edu/hpcc/help/)