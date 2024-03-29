#include "rotate.h"
#include "main.h"
#include "gpio.h"

int r_front=0;
int r_behind=0;
//*******************************爪子*********************************

void openFront()  // 前面爪子张开
{
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_6,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_7,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,200);
	HAL_Delay(200);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,0);
	HAL_Delay(20);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,200);
	HAL_Delay(300);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,0);
}

void  closeFront()   // 前面爪子合上
{
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_6,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_7,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,200);
	HAL_Delay(200);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,0);
	HAL_Delay(20);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,200);
	HAL_Delay(600);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_1,0);
}

void openBehind()   // 后面爪子张开
{
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_8,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_11,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_2,200);
	HAL_Delay(450);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_2,0);
}

void closeBehind()   // 后面爪子合上
{
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_8,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOF,GPIO_PIN_11,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_2,200);
	HAL_Delay(500);
	__HAL_TIM_SetCompare(&htim9,TIM_CHANNEL_2,0);
	
}


// ****************************************转动**************************************

void clockwiseFront()   // 前面顺时针转90°
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(300);  // 230(1)
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}

void clockwiseFront_after()   
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(305);  // 230(1)
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}

void clockwiseFront_turn()   
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(300);  // 230(1)
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}


void anticlockwiseFront()   // 前面逆时针转90°
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(300);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}
void anticlockwiseFront_after()   // 前面 先顺90�  逆时针转90°
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(305);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}
void anticlockwiseFront_turn()   // 前面 先顺90? 逆时针转90°
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(300);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}


void halfcirlceFront()    // 前面转180°
{
	r_front++;
	if(r_front%2==0)
	{
			HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_SET);
			HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);
	}
	else
	{
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_RESET);
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_SET);
	}
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(600);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}


void halfcirlceFront_turn()    // 
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_2,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,200);
	HAL_Delay(600);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_3,0);
}


void anticlockwiseBehind()   // 后面逆时针转90°
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(300);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}

void anticlockwiseBehind_after()   
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(305);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}

void anticlockwiseBehind_turn()   
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(300);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}



void clockwiseBehind()  // 后面顺时针转90°
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(300);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}

void clockwiseBehind_after()  
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(305);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}

void clockwiseBehind_turn()  
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_SET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(300);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}


void halfcirlceBehind()   // 后面转180°
{
	r_behind++;
	if(r_behind%2==0)
	{
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
		HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_RESET);
	}
	else
	{
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_RESET);
		HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_SET);
	}
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(600);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}

void halfcirlceBehind_turn()   // 
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_5,GPIO_PIN_RESET);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,200);
	HAL_Delay(605);
	__HAL_TIM_SetCompare(&htim2,TIM_CHANNEL_2,0);
}

// ********************组合********************************
void front_clockwise_and_back()
{
	clockwiseFront();
	openFront();
	anticlockwiseFront_after();
	closeFront();
}

void front_anticlockwise_and_back()
{
	anticlockwiseFront();
	openFront();
	clockwiseFront_after();
	closeFront();
}

void behind_clockwise_and_back()
{
	clockwiseBehind();
	openBehind();
	anticlockwiseBehind_after();
	closeBehind();
}

void behind_anticlockwise_and_back()
{
	anticlockwiseBehind();
	openBehind();
	clockwiseBehind_after();
	closeBehind();
}

void turn1()   // F->B
{
	openBehind();
	//halfcirlceFront_turn();
	halfcirlceFront();
	closeBehind();
}

void turn2()    // U->D
{
	openFront();
	//halfcirlceBehind_turn();
	halfcirlceBehind();
	closeFront();
}

void turn3()  // L->B  B->R
{
	openBehind();
	clockwiseFront_turn();
	closeBehind();
	HAL_Delay(200);
	openFront();
	anticlockwiseFront_after();
	closeFront();
}

void turn4()  // B->L  R->B
{
	openBehind();
	anticlockwiseFront_turn();
	closeBehind();
	HAL_Delay(200);
	openFront();
	clockwiseFront_after();
	closeFront();
}

