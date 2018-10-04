//
//  Answers and grading instructions for CSci 1913 Lab 4
//  TOP SECRET FOR CSCI 1913 TA's ONLY!
//
//  James B. Moen
//  13 Feb 17
//
//  This lab asks students to rewrite the Python ZILLION class from Lab 2 in
//  Java. It has to be easy, because I've talked about Java code in class for
//  only days before the students see this lab. Students who already know Java
//  can probably do this in a few minutes; students who do not may take longer.
//

//  ZILLION. A multi-digit counter.

class Zillion
{
  private int[] digits;  //  The digits themselves.

//  Constructor. Make a new instance of ZILLION that can hold SIZE digits. We
//  assume SIZE is greater than or equal to 0.

  public Zillion(int size)
  {
    digits = new int[size];
  }

//  INCREMENT. Add 1 to the counter in DIGITS. We move right to left, turning
//  9's into 0's, until we run out of digits or until we find a digit that is
//  not a 9. In the latter case we add 1 to that digit.
//
//  This must use local variables (except for DIGITS).

  public void increment()
  {
    int index = digits.length - 1;
    while (index >= 0 && digits[index] == 9)
    {
      digits[index] = 0;
      index -= 1;
    }
    if (index >= 0)
    {
      digits[index] += 1;
    }
  }

//  TO STRING. Convert DIGITS to a string and return it.
//
//  This must use local variables (except for DIGITS).

  public String toString()
  {
    String temp = "";
    for (int index = 0; index < digits.length; index += 1)
    {
      temp += digits[index];
    }
    return temp;
  }
}

//  DRIVER. The MAIN method has tests for your class ZILLION. Each test has a
//  comment that shows what the test should print if your code is correct. It
//  also has the number of points you will receive if the test is successful.
//  These tests are worth a total of 25 points.

class Driver
{
  public static void main(String[] args)
  {
    Zillion z = new Zillion(2);
    System.out.println(z);  //  00  2 points

    z.increment();
    System.out.println(z);  //  01  2 points

    z.increment();
    System.out.println(z);  //  02  2 points

    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();

    System.out.println(z);  //  10  2 points
    z.increment();
    System.out.println(z);  //  11  2 points

    z = new Zillion(4);
    System.out.println(z);  //  0000  2 points

    for (int j = 1; j <= 999; j += 1)
    {
      z.increment();
    }
    System.out.println(z);  //  0999  2 points

    z.increment();
    System.out.println(z);  //  1000  2 points

    for (int j = 1; j <= 999; j += 1)
    {
      z.increment();
    }
    System.out.println(z);  //  1999  2 points

    z.increment();
    System.out.println(z);  //  2000  2 points

    for (int j = 1; j <= 7999; j += 1)
    {
      z.increment();
    }
    System.out.println(z);  //  9999  2 points

    z.increment();
    System.out.println(z);  //  0000  2 points

    z.increment();
    System.out.println(z);  //  0001  1 point
  }
}
