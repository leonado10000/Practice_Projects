#include<stdio.h>
#include<stdlib.h>
#define MAX_typeA 8     //room code 1

#define MAX_typeB3 15   //room code 2
#define MAX_typeB2 40   //room code 3

#define MAX_typeC2 20   //room code 4
#define MAX_typeC1 60   //room code 5

int curr_A=0;
int curr_B3=0;
int curr_B2=0;
int curr_C2=0;
int curr_C1=0;





//================================================================================================================================================================================================================
//================================================================================================================================================================================================================

//                                                                          VENKATESH RAYUDU :
//                                                               ADD COMMENTS AND DISPLAY COMMENTS FUNCTIONS

//================================================================================================================================================================================================================
//================================================================================================================================================================================================================


void comments(){
struct feedback{
        char Room_ID_Feedback[1000];
        struct feedback *next;
    }*feed,*feedback,*temp=NULL,*first=NULL,*last=NULL;
void creatr(){
    temp=(struct feedback*)malloc(sizeof(struct feedback));
            printf("Enter the Room_ID\n");
            scanf("%c",temp->Room_ID_Feedback);
            temp->next=NULL;
}
void creatf(){
    temp=(struct feedback*)malloc(sizeof(struct feedback));
    printf("Enter the Feedback\n");
    scanf("%c",temp->Room_ID_Feedback);
}

void creat(){
    for(int i=1;i<=2;i++){
        if(i==1){
            if(first==NULL){
                creatr();
                first=temp;
                last=first;
                printf("Room_ID:%c",Room_ID_Feedback);
            }
            else{
                creatr();
                temp->next=first;
                first=temp;
                printf("Room_ID:%c",Room_ID_Feedback);
            }
        }
    else{
        if(first==NULL){
                creatr();
                first=temp;
                last=first;
                printf("Room_ID:%c",Room_ID_Feedback);
            }
            else{
                creatr();
                temp->next=first;
                first=temp;
                printf("Room_ID:%c",Room_ID_Feedback);
            }
            
        }
    }
}
}

        



//==============================================================================================================
//                          MAIN FUNTION
//========================================================================================================
void main(){
    int ch=1,choice;
    char pref;
    while(ch){
        printf("Menu\n1.Add guest\t2.Add comment\nEnter choice:");
        scanf("%d",&choice);
        switch(choice){
        /*    case 1:
                Enter_dets();
                break;*/
            case 2:
                printf("\nEnter the comment you want to add");
                comments();
                break;
        }
    }
}
