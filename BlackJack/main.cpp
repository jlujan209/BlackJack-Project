#include <iostream>
#include <fstream>
#include "Dealer.h"

using namespace std;

int main() {
	ifstream cardsInp("cards.txt");
	int num; 
	string cardName;

	while (cardsInp >> num >> cardName) {
		cout << num << " " << cardName << endl;
	}

	cardsInp.close();

	return 0;
}