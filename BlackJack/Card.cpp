#include "Card.h"

Card::Card(){
	this->cardNumber = -1;
	this->cardType = "Undefined";
}
Card::Card(int num, string type) {
	this->cardNumber = num;
	this->cardType = type;
}
int Card::getCardNumber() {
	return this->cardNumber;
}
string Card::getCardType() {
	return this->cardType;
}
void Card::setCardNumber(int x) {
	this->cardNumber = x;
}
void Card::setCardType(string type) {
	this->cardType = type;
}