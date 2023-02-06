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


void comment(){
    struct feedback{
        int Room_ID;
        char Feedback[1000];
        struct feedback *next;
    };
    typedef struct feedback *feed;
    void comment_feed(){
        feed temp=(struct feedback *)malloc(sizeof(Struct feedback));
        printf("Enter the Room_ID\n");
        scanf("%d",&temp->Room_ID);
        printf("Enter the feedback\n");
        scanf("%s",&temp->Feedback);
        printf("Room_ID:"%d"\nFeedback:"%s,temp->Room_ID,temp->Feedback);
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
            case 1:
                Enter_dets();
                break;
            case 2:
                printf("Enter the comment you want to add");
                break;
        }
    }
}
