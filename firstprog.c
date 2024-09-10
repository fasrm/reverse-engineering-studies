/*
gcc firstprog.c
ls -l a .out
./a.out

objdump -D a.out | grep -A20 main.:
*/

#include <stdio.h>

int main()
{
  int i;
  for(i=0; i<10; i++)           // Loop 10 times.
  {
    puts("Hello, world!\n");    // put the string to the output.
  }
  return 0;                     // Teel OS the program exited without errors.
}
