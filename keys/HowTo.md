openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out CertificateRedes2020.crt -keyout KeyRedes2020.key

-newkey rsa:4096: Create a 4096 bit RSA key for use with the certificate. RSA 2048 is the default on more recent versions of OpenSSL but to be sure of the key size, you should specify it during creation.

-x509: Create a self-signed certificate.

-sha256: Generate the certificate request using 265-bit SHA (Secure Hash Algorithm).

-days: Determines the length of time in days that the certificate is being issued for. For a self-signed certificate, this value can be increased as necessary.

-nodes: Create a certificate that does not require a passphrase. If this option is excluded, you will be required to enter the passphrase in the console each time the application using it is restarted
