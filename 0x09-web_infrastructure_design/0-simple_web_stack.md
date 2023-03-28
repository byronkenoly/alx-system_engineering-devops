## Specifics about this infrastucture

+ What is a server? A server is a piece of computer hardware or software that provides functionality for other programs or devices called clients.

+ What is the role of the domain name? One will have a difficult time remembering IP addresses compared too domain names.

+ What type of DNS record `www` is in `www.foobar.com` ? It is an A record. A records create a DNS record that points to an IPv4 address. It allows us to use mnemonic names such as `www.foobar.com` in place of IP addresses like `8.8.8.8`

+ What is the role of the web server? A web server handles incoming HTTP requests from clients(such as web browsers) and sends them to application server for processing

+ What is the role of the application server? The application server is responsible for executing the code that processes the requests received from the web server.

+ What is the role of the database? The database is responsible for storing and managing the application data.

+ What is the server using to communicate with the computer of the user requesting the website? TCP/IP protocol governs the communication between computers

## Issues with this infrastructure

+ Single Point Of Failure(SPOF). The system is not redundant. There is only one web server and database. If the web server or the database fails there is no other alternative to take its place.
