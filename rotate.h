#ifndef __ROTATE_H
#define __ROTATE_H	

#include "main.h"
#include "tim.h"

extern void closeFront(void);
extern void openFront(void);
extern void closeBehind(void);
extern void openBehind(void);

extern void clockwiseFront(void);
extern void anticlockwiseFront(void);
extern void halfcirlceFront(void);
extern void anticlockwiseFront_after(void);
extern void clockwiseFront_after(void);  
extern void halfcirlceFront_turn(void);

extern void clockwiseBehind(void);
extern void anticlockwiseBehind(void);
extern void halfcirlceBehind(void);
extern void clockwiseBehind_after(void);
extern void anticlockwiseBehind_after(void);
extern void halfcirlceBehind_turn(void);

extern void front_clockwise_and_back(void);
extern void front_anticlockwise_and_back(void);
extern void behind_clockwise_and_back(void);
extern void behind_anticlockwise_and_back(void);

extern void turn1(void);
extern void turn2(void);
extern void turn3(void);
extern void turn4(void);

extern int time;

#endif 
