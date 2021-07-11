#include <unistd.h>
#include <stdio.h>

#define O_RDONLY         00

int main(){
    int fd;
    fd = open("/dev/inc", O_RDONLY);
    while(1) {
        unsigned int in_vari = 12;
        unsigned int out_vari = 0;

        out_vari = read(fd, &in_vari, sizeof(in_vari));

        printf("%d\n", out_vari);
        sleep(1);
    }
}