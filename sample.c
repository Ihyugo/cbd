#include <stdio.h>
int main(void){
	int  i=0;
	double sum=0.0,total=0.0;
	for(i=0;i<100000000;i++){
		sum = (2*i + 1);
		if(i % 2 == 0){
		total += 1/sum;
		}else{
		total -= 1/sum;
		}
	}
		printf("%f\n" ,4*total);
}
