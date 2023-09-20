/* A standard library provides capabilities to perform a task
iostream = input-output stream to input and output values*/

// #include <iostream> //Preprocessor directive

/* int is the type of value to be returned
main() is the initial function in which parameters are written inside () */

// int main()

// code start
// {
//	std::cout << "Hello World!"; // a statement

	//semicolon (;) is used to indicate the termination of a statement
	//std is like a container of features imported from above libraries
	//cout = characters out = to output lots of characters on the screen	

//	return 0; /*program terminated correctly - any + ve or -ve integer
//	indicates our program encountered error */
//}


/*#include <iostream>
int main()
{
	int file_size = 100; //file_size is a varible storing integer value
	double sales = 9.99;
	std::cout << file_size;
	std::cout << sales;
	return 0;
}*/

/*#include <iostream>
int main()

{
	int a = 1;
	int b = 2;

	int temp = b;
	b = a;
	a = temp;

	std::cout << a;
	std::cout << b;
	return 0;
}*/


/* #include <iostream>
int main()
{
	const double pi = 3.14;
//	pi = 10; // ERROR: you cannot assign a value to a variable (pi) that is CONSTANT 
	std::cout << pi;	 
} */


// NAMING CONVENTIONS

/*#include <iostream>
int main()

{
	int file_size; //SNAKE Case
	int FileSize; //PASCAL Case
	int fileSize; //CAMEL Case
	int iFileSize; //Hungarian Notation | Here, i = integer (data type)
}*/



// ADDITION, SUBTRACTION, MULTIPLICATION

/*#include <iostream>
int main()
{
	int x = 4;
	int y = 6;
	int a = x + y;
	int b = x - y;
	int c = x * y;
	
	std::cout << a;
	std::cout << b;
	std::cout << c;
}*/


// DIVISION

/*#include <iostream>
int main()
{
	int x = 11;
	int y = 2;
	int m = x / y;  //Answer: 5 [division of two integers will give an integer plus m is also an integer]
	int n = x % y;  //Answer: 1 [remainder of division of 11 and 2]

	double a = 11;
	int b = 2;
	double c = a / b;

	std::cout << m;
	std::cout << n;
	std::cout << c;

}*/


// MATHEMATICAL CALCULATION

/*#include <iostream>
int main()
{
	int x = 10;
	x = x + 5;;
	std::cout << x << '\n';
	x++; // increment by 1
	std::cout << x << '\n';

	x = x - 3;
	std::cout << x << '\n';
	x--; // decrement by 1
	std::cout << x << '\n';

	int y = 3;
	y = y * 2;
	std::cout << y << '\n';
//	y**; // ONLY POSSIBLE FOR INCREMENT (++) AND DECREMENT (--) by 1
	std::cout << y << '\n';

	int m = 10;
	int n = m++; //'n' assigned with m, then m is incremented [n = 10, m = 11]
	std::cout << "The value of m is " << m << '\n';
	std::cout << "The value of n is " << n << '\n';

	int p = 10;
	int q = ++p; //'p' is incremented and then assigned to 'q' [p = 11, q = 11]
	std::cout << "The value of p is " << p << '\n';
	std::cout << "The value of q is " << q << '\n';

}*/

/*#include <iostream>
int main()

{
	double x = 10;
	double y = 5;
	double z = (x + 10) / (3 * y);
	std::cout << "The value of z is " << z << '\n';
}*/



/*#include <iostream>
using namespace std; // NOT required to write "std" anymore in program

int main()
{
	int x = 10;
	cout << "The value of x is " << x;
}
*/

/*#include <iostream>
using namespace std;   //ALTERNATIVE: using std::cout;

int main()
{
	int sales = 95000;
	const double state_tax_rate = 0.04;
	double state_tax = state_tax_rate * 95000;

	const double county_tax_rate = 0.02;
	double county_tax = county_tax_rate * 95000;
	double total_tax = state_tax + county_tax;

	cout << "Total Sales = $" << sales << '\n';
	cout << "State tax = $" << state_tax << '\n';
	cout << "County tax = $" << county_tax << '\n';
	cout << "Total tax to be paid = $" << total_tax << '\n';
}*/


// (cin) >> STREAM EXTRACTION OPERATOR  (cout) << STREAM INSERTION OPERATOR 

/*#include <iostream>
using namespace std;

int main()
{
	cout << "Enter a value of num = ";
	int value;
	cin >> value;
	
	cout << "Enter the second value = ";
	float num;
	cin >> num;

	cout << "The first value is " << value << '\n';
	cout << "The second value is " << num << '\n';

	cout << "Enter x & y = ";
	float x;
	float y;
	cin >> x;
	cin >> y;
	cout << "The sum of " << x << " and " << y << " is " << x + y << '\n';

	cout << "Enter a & b = ";
	float a;
	float b;
	cin >> a >> b;
	cout << "The product of a and b is " << a*b << '\n';
}*/



/*#include <iostream>
#include <cmath> // <cmath> library provides a set of functions and constants for mathematical operations.
using namespace std;

int main()
{
	double uvalue = ceil(1.8);
	cout << "The upper rounded value of 1.8 is " << uvalue << '\n';
	
	double lvalue = floor(1.8);
	cout << "The lower rounded value of 1.8 is " << lvalue << '\n';

	double absolute = abs(-12);
	cout << "The absolute value of -12 is " << absolute << '\n';

	double sqroot = sqrt(16);
	cout << "The square root of 16 is " << sqroot << '\n';

	double power = pow(3, 4);
	cout << "3 to the power of 4 is " << power << '\n';

	double rnv = round(1.5);
	cout << "The rounded value of 1.5 is " << rnv << '\n';

	double sinv = sin(0); // DOES NOT WORK
	cout << "The sin of 0 is " << sinv << '\n';

	double remainder = fmod(11, 3);
	cout << "The remainder of 11/3 is " << remainder << '\n';

	const double pie = 3.14;
	cout << "Enter the radius of circle = ";
	int r;
	cin >> r;
	double area = pie * pow(r,2);
	cout << "The area of circle is " << area;
}*/


/*#include <iostream>
using namespace std;

int main()
{
	double price = 99.99;
	float interestRate = 3.67f; //'f' in 3.67 tells us float; default is 'double'
	long fileSize = 90000L; //'L' in 90000 tells us Large; default is 'int'
	char letter = 'a';
	bool isValid = false;
	auto val = 9.99f //"auto" type tells us "float"
	return 0
}*/



/*#include <iostream>
using namespace std;

int main()
{
	//int number = 1.2; //OUTPUT = 1
	//int number { 1.2 }; //NO Output
	//int number {}; //Output = 0
	//int number; //Error = Variable Uninitialized
	
	cout << number << '\n';
}*/



/*#include <iostream>
using namespace std;

int main()
{
	int numb = 0b11111111;
	int numh = 0xFF;
	
	cout << "Binary's equivalent is " << numb << '\n';
	cout << "Hexadecimal's equivalent is " << numh << '\n';
}*/


/*#include <iostream>
using namespace std;

int main()
{
	int number = 0b11111111; //Answer: 255 | "0b" represents hexadecimal
	int hexa = 0xff; //Answer: 255 | "0x" represents hexadecimal
	cout << "hexadecimal value is" << hexa << '\n';
	cout << "binary conversion is" << number << '\n';
	return 0;
}*/





/*FUNDAMENTAL TYPES

short => 2 bytes => Range of numbers = -32k to +32k
int => 4 bytes => Range of numbers = -2B to +2B
long => 4 bytes => Same As Above
long long => 8 bytes

float => 4 bytes
double => 8 bytes
long double => 8 bytes

bool => 1 byte
char => 1 byte
*/





/*
#include <iostream>
using namespace std;

int main()
{
	int number = 1'000'000; //From 4 bytes
	short another = number; //To 2 bytes
	cout << another << '\n';
}*/
//OUTPUT = 16960 (Data Loss during conversion from 4 bytes to 2 bytes)(Narrowing Down)


/*
#include <iostream>
using namespace std;

int main()
{
	short value = 30'000; //From 2 Bytes
	int second = value; //To 4 Bytes
	cout << second << '\n';
}*/
//OUTPUT = 30000 (NO Data Loss during conversion from 2 bytes to 4 bytes - NO Narrowing Down)


/*
#include <iostream>
#include <cstdlib> //random number generation
#include <ctime> //time manipulation, time formatting, and measuring time intervals

using namespace std;

int main()
{
	long elapsed_seconds = time(0); //Jan 1, 1970

	cout << "The elapsed seconds since January 1, 1970 is "<< elapsed_seconds << '\n';
	srand(elapsed_seconds); //seed the random number generator

	int rnum = rand() % 10; //num based on mathematical formula, so same in every execution
	cout << rnum;
	return 0;
}*/

//use std::time(nullptr) to obtain the current time




//Roll a DIE at a time
/*
#include <iostream>
#include <cstdlib> //random number generation
#include <ctime> //time manipulation, time formatting, and measuring time intervals

using namespace std;

int main()
{
	const int minvalue = 1;
	const int maxvalue = 6;
	
	srand(time(0));
	int die=(rand() % (maxvalue - minvalue + 1)) + minvalue;

	cout << "die roll is " << die;

}*/
/*
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string name;
	name = "pappu jha";
	cout << name << '\n';

	string new_name = name + " is in USA";
	cout << new_name << '\n';
}*/


// TRUE = 1, FALSE = 0
/*
#include <iostream>
using namespace std;

int main()
{
	int x = 3, y = 4;
	bool a, b, c, d, e, f, g, h, i, j;

	a = (x == 3);
	cout << "a = " << a << '\n';

	b = (x != 3);
	cout << "b = " << b << '\n';

	c = (x >= y);
	cout << "c = " << c << '\n';

	d = (x < y);
	cout << "d = " << d << '\n';

	e = (a && b); //AND
	cout << "e = " << e << '\n';

	f = (a || b); //OR
	cout << "f = " << f << '\n';

	g = (x != y); // (!=)NOT EQUAL TO
	cout << "g = " << g << '\n';

	h = !(y==4); // !(NOT)
	cout << "h = " << h << '\n';
	
	i = !0;
	cout << "i = " << i << '\n';

	j = !1;
	cout << "j = " << j << '\n';

	int m = 3;
	m += 1;
	cout << "m = " << m << '\n';

	int n = 3;
	n -= 1;
	cout << "n = " << n << '\n';

	int o = 3;
	o *= 4;
	cout << "o = " << o << '\n';

	int p = 12;
	p /= 4;
	cout << "p = " << p << '\n';

	int ax = 17;
	ax %= 2;
	cout << "value of ax = " << ax;

	int r = 8, s = 9;
	int t = (8 < 9) ? r : s; //True, Answer: r(8)
	cout << "t = " << t << '\n';

	int u = (8 > 9) ? r : s; //False, Answer: s(9)
	cout << "u = " << u << '\n';

	float v = 3.14;
	int w = int(v);       // w = 3
	cout << "w = " << w << '\n';

	int z = sizeof('BCDE');
	cout << "z = " << z; 
}*/

/*
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string a;
	cout << "Enter a string = " << '\n';
	//cin >> a;         //Only ONE word is accepted as INPUT if given too many
	
	getline (cin, a); //all words are accepted as input string
	cout << "a is = " << a << '\n';
}*/




//USE OF "endl"

/*#include <iostream>
using namespace std;

int main()
{
	cout << "Hi! I'm Pappu Jha" << endl;
	cout << "I study at USM in USA" << endl;

	return 0;
}*/



// '\n' can be put inside double quote " " too 
/*
#include <iostream>
#include <string>

using namespace std;

int main()
{
	cout << "My Name is Pappu Jha \n";
	cout << "Here, I am in the USA \n";
	
	string str0, str1, tmpStr, str2;

	cin >> str0;
	cin >> str1;
	getline(cin, tmpStr);
	getline(cin, str2);

	cout << "str0 = " << str0 << '\n' << "str1 = " << str1 << '\n' << "tmpStr = " << tmpStr << '\n' << "str2 = " << str2 << endl;
	return 0;
}*/



/*
#include <iostream>

using namespace std;

int main()
{
	float temp;
	cout << "Enter the temperature = ";
	cin >> temp;

	if (temp <= 32)
	{
		cout << "Freezing outside" << endl;
	}
	else
	{
		cout << "NOT Freezing outside" << endl;
	}
}*/

/*
#include <iostream>
using namespace std;

int main()
{
	int temp;
	cout << "Enter temperature: ";
	cin >> temp;

	if (temp <= 32)
		cout << "Freezing outside" << endl;

	else if (temp <= 55)
		cout << "Not freezing but wear a coat" << endl;

	else if (temp < 70)
		cout << "Chilly" << endl;

	else if (temp <= 85)
		cout << "warm - wear light clothing" << endl;

	else
		cout << "Hot - hit the beach" << endl;
}*/



/*
#include <iostream>
using namespace std;

int main()
{
	int num;
	cout << "Enter a number between 1 and 4: ";
	cin >> num;

	switch (num)
	{
	case 1:
		cout << "Roman Numeral: I\n";
		break;
	
	case 2:
		cout << "Roman Numeral: II\n";
		break;

	case 3:
		cout << "Roman Numeral: III\n";
		break;

	case 4:
		cout << "Roman Numeral: IV\n";
		break;
	
	default:
		cout << "Oops! Only convert numbers between 1 and 5\n";
		break;
	}
}*/



/*
#include <iostream>
using namespace std;

int main()
{
	int num, count = 0;
	char next = 'y';

	cout << "Multiplication Table\n";

	cout << "Give me a number: ";
	cin >> num;

	while (next == 'y')
	{
		cout << num << "*" << count;
		cout << " = " << num * count << "\n";

		count++;

		cout << "Next Multiple (y/n)? = ";
		cin >> next;
	}

	cout << "Finished \n";
}*/



/*
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int num;
	cout << "Enter number whose table to write = ";
	cin >> num;

	for (int count = 0; count < 11; count++)
	{
		cout << num << "*" << count << " = " << setw (8) << num * count << endl;
	}
	cout << "Finished!";
}*/
// setw() function is used to add space for the next value - parameter represents the size of space


/*
#include <iostream>
using namespace std;

int main()
{
	int choice = 1;
	do
	{
		cout << "Pappu \n";
		cout << "Roshan \n";
		
		cout << endl;
		cout << "Enter choice = ";
		cin >> choice;
		cout << endl;
	}
	while (choice >= 1 && choice <= 3);
}*/


/*
#include <iostream>
using namespace std;

int main()
{
	int num;
	cout << "Enter a number: ";
	cin >> num;

	switch (num)
	{
	case 1:
		cout << "Roman Number > I \n";
		break;

	case 2:
		cout << "Roman Number > II \n";
		break;

	case 3:
		cout << "Roman Number > III \n";
		break;
		
	default:
		cout << "Enter a number between 1 and 10 only \n";
		break;
	}
}*/

/*
#include <iostream>
using namespace std;

int main()

{
	int num_day;
	cout << "Enter the number of working days = ";
	cin >> num_day;

	int total_pay = 0;

	for (int day = 1; day <= num_day; day++)
	{
		cout << "Pay for day " << day << " = " << pow(2, day) << " cents" << endl;
		total_pay += pow(2, day);
	}
	cout << " " << endl;
	cout << "Total pay for " << num_day << " days = " << total_pay << " cents = $" << float(total_pay)/100;
	cout << " " << endl;
}*/


/*
#include <iostream>
using namespace std;

int main()
{
	cout << "Enter the temperature in Fahrenheit = ";
	int fahrenheit;
	cin >> fahrenheit;

	double celsius;
	celsius = (fahrenheit - 32) * (float (5) / float (9));
	cout << "The temperature in celsius is " << celsius << '\n';

	double kelvin;
	kelvin = celsius + 273.15;
	cout << "The temperature in kelvin is " << kelvin << '\n';
}*/

/*
#include <iostream>
using namespace std;

int main()
{
	int row = 0;
	while (row < 3)
	{
		int col = 0;
		while (col < 2)
		{
			cout << "Enter your name: ";
			string name;
			cin >> name;
			cout << "name at row " << row << " and column " << col << " is " << name << endl;
			cout << endl;
			col += 1;
		}
		row += 1;
	}
}*/

/*
// At first, function int() is executed then other one - no matter what order the code is written in

#include <iostream>
using namespace std;

int fun_square_num(int num);

int main()
{
	int square_num;
	square_num = fun_square_num(7);
	cout << "Square of 7 is " << square_num << endl;
}

int fun_square_num(int num)
{
	int square_num = num * num;
	return square_num;
}*/


/*
#include <iostream>
using namespace std;

int fun_weight(int weight)
{
	int cost;
	if (weight < 10) {
		cost = 50;
	}
	else {
		cost = 100;
	}
	return cost;
}

int main()
{
	int weight;
	cout << "Enter the weight = ";
	cin >> weight;
	int cost = fun_weight(weight);
	cout << "Cost of the weight " << weight << " units is " << cost << endl;
}*/


/*
#include <iostream>
using namespace std;

int fun_area(int length)
{
	int area;
	area = length * length;
	return area;
}

int main()
{
	int length;
	cout << "Enter length = ";
	cin >> length;

	int area;
	area = fun_area(length);
	cout << "The area is " << area << endl;
}*/



/*
#include <iostream>
void modifyValue(int &num) 
// with '&', the original variable is affected - without it, NOT

{
	num = num * 2;
}

int main()
{
	int myNumber = 5;

	std::cout << "Original value: " << myNumber << std::endl;

	// Call the function with myNumber passed by reference.
	modifyValue(myNumber);

	std::cout << "Modified value: " << myNumber << std::endl;

	return 0;
}*/


/*
#include <iostream>
using namespace std;

int main()
{
	const int index = 5;
	int oldestPeople[index];

	int i = 0;
	while (i <= 4)
	{
		cout << "Enter value: ";
		cin >> oldestPeople[i];
		i += 1;
	}

	cout << endl;
	cout << oldestPeople << endl;
	cout << endl;

	for (int i = 0; i <= 4; i++)
		cout << "value in array oldestPeople at index " << i << " = " << oldestPeople[i] << endl;
}

int main()
{
	int myArray[3] = { 5, 7, 11 };
	
	for (i=0; while)
}
*/


/*
#include <iostream>
using namespace std;

int main()
{
	string name;
	cout << "Enter name: ";
	cin >> name;

	if (name == "pappu")
		cout << "FOUND";
	else
		cout << "Oops!";

	cout << endl;
}*/


/*
#include <iostream>
using namespace std;

int main()
{
	for (int i = 1; i <= 5; i++)
	{
		int after_index, before_index, initial;

		initial = i;
		after_index = i++; //after_index = i, then 'i' is incremented by 1
		i = initial;
		before_index = ++i; //'i' is incremented by 1 then before_index = i 

		cout << "i = " << initial << "  after = " << after_index << "  before = " << before_index << endl;
		i = initial;
	}
}
*/
/*
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
	cout << fixed << setprecision(1);
//floating-point numbers will be displayed with one digit after the decimal point.
}*/


/*
#include <iostream>
using namespace std;

const int week = 7;

int main()
{
	float tempf[week];
	float tempc[week];
	string days[week] = { "sunday","monday","tuesday","wednesday","thursday","friday","saturday" };
	
	for (int i = 0; i < week; i++) {
		cout << "Enter the temperature in Fahrenheit for " << days[i] << " = ";
		cin >> tempf[i];
		tempc[i] = (5.0 / 9.0) * (tempf[i] - 32);
		cout << "The equivalent temperature of " << tempf[i] << " degree Fahrenheit is " << tempc[i] << endl << endl;
	}
	float sum = 0;
	for (int j = 0; j < week; j++) {
		sum += tempf[j];
	}
	float fr = sum / week;
	float cel = (5.0 / 9.0) * (fr - 32);

	cout << "The average temperature in Fahrenheit = " << round(fr) << endl;
	cout << "The average temperature in Celsius = " << round(cel) << endl;
}
*/


/*
#include <iostream>
using namespace std;

int length;
int breadth;

int farea(int length, int breadth) {
	int area = length * breadth;
	return area;
}

int main() {
	cout << "Enter length = ";
	cin >> length;

	cout << "Enter breadth = ";
	cin >> breadth;

	int area = farea(length, breadth);
	cout << "The area of rectangle is " << area;
}*/

/*
#include <iostream>
using namespace std;

int swap_num(int& val1, int& val2);

int main()
{
	int num1, num2;

	cout << "Enter num1 = ";
	cin >> num1;

	cout << "Enter num2 = ";
	cin >> num2;

	swap_num(num1, num2);

	cout << "After num1: " << num1 << "\n";
	cout << "Before num2: " << num2 << "\n";
}

//Passing parameters val1 and val2 by reference

int swap_num(int &val1, int &val2)
{
	int temp = val1;
	val1 = val2;
	val2 = temp;
	return val1, val2;
}*/


/*
#include <iostream>
#include <string>

using namespace std;

int main()
{
	for (int i = 0; i < 5; i++) {
		
		string coin_side;
		cout << "Enter the side of coin: head or tail = ";
		cin >> coin_side;

		if (coin_side == "head")
			cout << "True" << endl << endl;
		else if (coin_side == "tail")
			cout << "False" << endl << endl;
		else
			cout << "Print valid input" << endl << endl;
	}
}*/



/*
#include <iostream>
#include <string>
using namespace std;

const int total_days = 4;
const int rate = 12;

int main()
{
	string name;
	cout << "Enter name of person: Pappu or Roshan = ";
	cin >> name;

	if (name == "Pappu") {
		int num_hours[total_days] = { 6, 8, 3, 3 };
		int wage[total_days];
		int total = 0;

		for (int day = 0; day < total_days; day++) {
			wage[day] = num_hours[day] * rate;
			cout << endl << "The wage of day " << day + 1 << " is " << wage[day] << endl;
			total += wage[day];
		}
		cout << endl << "Total salary of this week is " << total << endl;
	}

	else if (name == "Roshan") {
		int num_hours[total_days];

		for (int day = 0; day < total_days; day++) {
			cout << endl << "Enter the hours worked on day " << day + 1 << " = ";
			cin >> num_hours[day];
		}
		int wage[total_days];
		int total = 0;

		for (int day = 0; day < total_days; day++) {
			wage[day] = num_hours[day] * rate;
			cout << endl << "The wage of day " << day + 1 << " is " << wage[day] << endl;
			total += wage[day];
		}
		cout << endl << "Total salary of this week is " << total << endl;
	}
	else
		cout << "Enter a Valid Name";
	
}*/


/*
#include <iostream>
#include <cstring>
using namespace std;


int fun_maxnum(int array_num[], int size)
{
	int max_num = array_num[0];

	for (int i = 1; i < size; i++) {
		if (array_num[i] > max_num)
			max_num = array_num[i];

	}
	return max_num;
}

int main()
{
	int array_num[] = { 10,8,12,5,16,3 };
	int size = 6;

	int max_num = fun_maxnum(array_num, size);

	cout << "Maximum  number in the array " << array_num << " is " << max_num;
}*/


/*
#include <iostream>
using namespace std;

int main()
{
	const int total_row = 2;
	const int total_column = 3;

	int mark[total_row][total_column] = { {10,12,14},{16,18,20} };

	for (int row = 0; row < total_row; row++) {
		for (int column = 0; column < total_column; column++) {
			cout << "The mark of row " << row << " and column " << column << " = " << mark[row][column] << endl;
		}
	}
}*/



// Word's LENGTH & INDEXING, not of all data types (array)
/*
#include <iostream>
#include <string>
using namespace std;

int main()
{
	string middle_name = "Kumar ";
	string name = "Pappu";
	cout << "Using .size(), length of " << name << " is " << name.size() << endl;
	cout << "Using .length(), length of " << name << " is " << name.length() << endl;
	cout << "INDEXING - 2nd letter of the word " << name << " is " << name[1] << endl;
	cout << "Updated word is " << name.insert(0, "Jha ") << endl;
	cout << "Final word is " << name + " " +middle_name << endl;
}*/


/*
#include <iostream>
#include <cctype>

using namespace std;

int main() {
	if (isalpha("c") == true)
		cout << "YES - TRUE" << endl;

	if (isupper("C") == true)
		cout << "YES - TRUE" << endl;

	if (isdigit("1") == true)
		cout << "YES - TRUE" << endl;

	if (isalpha("1") == true)
		cout << "YES - TRUE" << endl;
	else
		cout << "false"

}*/


/*
#include <iostream>
using namespace std;


int main()
{
	int num_arr[] = { 10,8,12,7,14,5,20 };
	int smallest_num = num_arr[0];
	int length = sizeof(num_arr) / sizeof(num_arr[0]); //LENGTH of ARRAY

	for (int i = 1; i < length; i++) {
		
		if (num_arr[i] < smallest_num) {
//			cout << "num_arr[i] = " << num_arr[i] << endl;
			smallest_num = num_arr[i];
		}
//		cout << "smallest num = " << smallest_num << endl;
	}
	cout << "The MINIMUM number in the array is " << smallest_num << endl;
/*
	for (const int& element : num_arr)
		std::cout << element << " ";*/	
/*
	float sum = 0;
	float count = 0;

	for (int i = 0; i < length; i++) {
		count = count + 1;
		sum = sum + num_arr[i];
	}		
	cout << "sum = " << sum << "\t" << "count = " << count << "\t" << "average = " << sum / count;
}*/




//LENGTH OF ARRAY
/*
#include <iostream>
using namespace std;


int main()
{
	int num[] = {10,11,9,8,12};
	int length = sizeof(num) / sizeof(num[0]);
	cout << "length = " << length << endl;

	for (int i = 0; i < length; i++) {
		cout << "value = " << num[i] << endl;
	}
	return 0;	
}*/



/*
#include <iostream>
using namespace std;

int main()
{
	int food[3][4] = { {10,17,13,12}, {28,24,26,21}, {32,34,41,40} };

	int sum = 0;
	int count = 0;
	double final_sum = 0;

	for (int r = 0; r < 3; r++) {
		int max_food_day = 0;

		for (int c = 0; c < 4; c++) {
			sum += food[r][c];
			count += 1;

			if (food[r][c] > food[r][max_food_day])
				max_food_day = c;
		}
		cout << "Dog " << r + 1 << "\t" << "=>  total is " << sum << "\t" << " count is " << count << "\t" << " average is " << sum/count << "\t" << "maximum food day = " << max_food_day << endl;

		final_sum += sum;
		sum = count = 0;
	}
	cout << endl;
	cout << "All dogs" << "\t" << "total food = " << final_sum << "\t" << "average food by each dog = " << final_sum / 3.0 << endl;
}*/



//CHECK PASSWORD VALIDITY
/*
#include <iostream>
using namespace std;

int main()
{
	string pw;
	cout << "Enter a password = ";
	cin >> pw;

	int length = pw.size();

	int count = 0;
	int ucount = 0;
	int lcount = 0;
	int ncount = 0;

	for (int i = 0; i < length; i++) {
		count += 1;

		if (pw[i] >= 'A' and pw[i] <= 'Z')
			ucount += 1;
		else if (pw[i] >= 'a' and pw[i] <= 'z')
			lcount += 1;
		else if (pw[i] >= '0' and pw[i] <= '9')
			ncount += 1;
	}
	if (count >= 6 && ucount >= 1 && lcount >= 1 && ncount >= 1)
		cout << "Valid Password";
	else
		cout << "Invalid Password";
}*/


/*
#include <iostream>
using namespace std;

int main()
{
	char correct_ans[] = {'A','D','B','B','C'};
	char user_ans[5];
	bool status = true;
	
	for (int i = 0; i < 5; i++) {
		cout << "Enter user answer = ";
		cin >> user_ans[i];

		if (user_ans[i] != correct_ans[i])
			cout << "Answer of question " << i << " NOT matched - FAIL";
			status = false;
			break;
	}
	if (status == true){                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            true{
		cout << "value found" << endl;
	}
	return 0;
}*/

/*
#include <iostream>
using namespace std;

int main()
{
	int value;
	int* address; //POINTER

	value = 5;
	address = &value;
	
	cout << "Variable value has " << value << endl;
	cout << "Address of value " << value << " is " << address << endl;
	cout << "Value stored at address " << address << " is " << *address << endl; //DEREFERENCING

	*address = 10;
	cout << "value at " << address << " *address is " << *address << endl;
	cout << "Variable value has " << value << endl;

	return 0;
}*/

/*
#include <iostream>
using namespace std;

int main()
{
	int num1 = 56, num2 = 81;
	int* ptr1;
	int* ptr2;

	ptr1 = &num1; //"ptr1" gets the address of "num1"

	for (int i = 0; i < 5; i++) {
		cout << "value of *ptr1 is " << *ptr1 << endl;
		*ptr1 += i;		
	}
	
	cout << "value of *ptr1 is " << *ptr1 << endl << endl;

	ptr2 = &num2; //"ptr2" gets the address of "num2"

	for (int i = 5; i > 0; i--) {
		cout << "value of *ptr2 is " << *ptr2 << endl;
		*ptr2 -= i;
	}

	int sum = *ptr1 + *ptr2;
	cout << "value of *ptr2 is " << *ptr2 << endl << endl;
	cout << "The sum of " << *ptr1 << " and " << *ptr2 << " is " << sum << endl;
	
	return 0;
}*/


/*
#include <iostream>
using namespace std;

int main()
{
	int arr[5] = { 78, 12, 96, 201, 128 };
//	int* ptr = arr;
	int* ptr = &arr[0];

	cout << "arr[0] = " << arr[0] << endl;
	cout << "*(arr) = " << * (arr) << endl;
	cout << "*(arr + 1) = " << * (arr + 1) << endl;
	cout << "*ptr = " << * ptr << endl;
}
*/



//DYNAMIC MEMORY ALLOCATION

#include <iostream>
using namespace std;

int main()
{
	int size;
	cout << "How many values you want in an array? = ";
	cin >> size;
	cout << endl;

	int* values = new int[size];
	
	//allocates 'size' number of memory for 'int' type and point to the first value of array using 'values'
	
	cout << "POINTER = " << values << endl << endl;

	for (int i = 0; i < size; i++) {
		cout << "Enter value " << i + 1 << " = ";
		cin >> values[i];
		cout << "POINTER = " << values[i] << endl;
	}
	cout << endl;

	for (int i = 0; i < size; i++) {
		cout << "Value " << i + 1 << " = " << values[i] << endl;
		cout << "POINTER = " << values << endl;
	}

	delete[] values; //DELLOCATING ARRAY
	cout << endl << "POINTER = " << values << endl << endl;

	cout << endl << "POINTER - Before nullptr = " << values << endl;
	values = nullptr; //pointer does not point to any accessible memory
	cout << "POINTER - After nullptr = " << values << endl;

	return 0;
}



// ARRAY IN REVERSE ORDER - DYNAMIC ALLOCATION
/*   
#include <iostream>
using namespace std;

int main()
{
	int size;
	cout << "How many values you want in an array? = ";
	cin >> size;
	cout << endl;

	int* values = new int[size];

	for (int i = 0; i < size; i++) {
		cout << "Enter value " << i + 1 << " = ";
		cin >> values[i];
	}
	cout << endl;
	for (int i = 0; i < size; i++)
		cout << "Value " << i + 1 << " = " << values[i] << endl;

	int* new_values = new int[size];

	for (int j = size - 1; j >= 0; j--)
		new_values[j] = values[j];
	
	cout << endl << "Values in REVERSE ORDER" << endl;

	for (int j = size - 1; j >= 0; j--)
		cout << "Value " << j + 1 << " = " << new_values[j] << endl;
}*/
