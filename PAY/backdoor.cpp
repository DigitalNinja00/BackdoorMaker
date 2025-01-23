#include<iostream>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<netinet/in.h>
#include<sstream>

using namespace std;

int main(){
	int sock = socket(AF_INET, SOCK_STREAM);
	if(sock<0){
		cerr<<"Error al crear el socket"<<endl;
	}
}