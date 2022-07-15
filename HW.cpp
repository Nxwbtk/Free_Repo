#include <iostream>
using namespace std;

int	a[10];

class myList
{
    public:
			int	i;
            int select;
            int	selectChoice()
            {
                cout << "==========Menu==========\n";
                cout << "+      1) Insert       +\n";
                cout << "+      2) Delete       +\n";
                cout << "+      3) Print        +\n";
                cout << "+      4) find         +\n";
				cout << "+      5) Exit         +\n";
                cout << "========================\n";
                cout <<  "   Please choose > ";
                cin >> select;
                return (select);
            }
			void	inSert(int insert)
			{
				i = 0;
				while (a[i])
				{
					a[i] = insert;
				}
			}
};

int main(void)
{
    myList	l_list;
    int		choice;
	choice = l_list.selectChoice();
	if (choice == 1)
	{
		int	ins;
		cout << "Please insert: ";
		cin >> ins;
		l_list.inSert(ins);
	}
	else if (choice == 2)
	{

	}
	else
		cout << "No choice!!\n";
}