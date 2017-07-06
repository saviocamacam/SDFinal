struct person {
	string name<>;
	string numTelefone<>;	
	person * previous;
	person * next;
};

struct list {
	person *first;
	person *last;
	int numPersons;
};

program MANAGER {
	version MANAGER_V1 {
		int ADD_PERSON(person) = 1;
		int REMOVE_PERSON(person) = 2;
	} = 1;
} = 0x2fffffff;
