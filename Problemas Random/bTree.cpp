#include <iostream>
using namespace std;

struct node {
	int data;
	node* left;
	node* right;
};

class bTree {
	public:
		btree();
		~btree();

		void insert(int data);
		node *search(int data);
		void destroy_tree();

	private:
		void destroy_tree(node *leaf);
		void insert(int data, node *leaf);
		node *search(int data, node *leaf);

		node *root;
}


