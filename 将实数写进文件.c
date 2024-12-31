#include<stdio.h>
#include<stdlib.h>

int main(void)
{
	FILE *fp;
	int n,i;
	double num;
	scanf("%d",&n);
	if((fp = fopen("Output_Data.txt","w")) == NULL){
		printf("Can not find the file!\n");
		exit(0);
	}
	for(i = 0;i < n;i++ ){
			scanf("%lf",&num);
			fprintf(fp,"%.6f\n",num);
	}
	if(fclose(fp)){
		printf("Can not close the file!\n");
		exit(0);
	}

}
