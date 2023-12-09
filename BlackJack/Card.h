#ifndef CARD_H
#define CARD_H
#include <string>
using namespace std;

class Card {
private:
	int cardNumber;
	string cardType;
public:
	Card();
	Card(int num, string type);
	int getCardNumber();
	string getCardType();
	void setCardNumber(int x);
	void setCardType(string type);
};

#endif 