/*
  llist printer RPC server implementation
  by Jeff Bezanson
*/

#include <stdlib.h>
#include "llist.h"
#include <string.h>

int result;
list *lst;

void createList() {
    lst = (list*)malloc(sizeof(list));
    lst->first = NULL;
    lst->last = NULL;
    lst->numPersons = 0;
}

void printList() {
    printf("print list");
    if(lst == NULL) {
        printf("Lista ainda vazia");
    }
    else {
        person * aux = lst->first;
        while(aux != NULL) {
            printf("nome: %s\n", aux->name);
            printf("num: %s", aux->numTelefone);
            aux = aux->next;
        }
    }
}

/* print out a list, returning the number of items printed */
int *add_person_1_svc(person *prs, struct svc_req *req)
{
    printf("Primeira linha");
    printList();    
    if(lst == NULL) {
            printf("lst is null");
        createList();
        if(lst == NULL)
            printf("Deu merda ao criar a lista. Por que? Nao sei\n");
    }
    
    if(lst->first == NULL && lst->last == NULL){
        lst->first = prs;
        lst->last = prs;
        lst->numPersons = lst->numPersons + 1;
        result = 1;
        return &result;
    }
    
    person * aux = lst->first;
    while(aux->next != NULL) {
        aux = aux->next;
    }
    aux->next = prs;
    prs->previous = lst->last;
    lst->last->next = prs;
    lst->last = prs;
    lst->numPersons = lst->numPersons + 1;
    
    result = 1;
    return &result;
}

int *remove_person_1_svc(person *prs, struct svc_req *req)
{
    result = 0;
    if(lst == NULL)
        return &result;
    else {
        person * aux = lst->first;
        if(aux == NULL)
            return &result;
        else {
            while(aux != NULL) {
                if(strcmp(aux->name,prs->name) == 0 && strcmp(aux->numTelefone,prs->numTelefone)) {
                    if(aux == lst->first && aux == lst->last) {
                        lst->first = NULL;
                        lst->last = NULL;
                    }
                    else if(aux == lst->first) {
                        lst->first = aux->next;
                        lst->first->previous = NULL;
                    }
                    else if(aux == lst->last) {
                        lst->last = aux->previous;
                        lst->last->next = NULL;
                    }
                    else {
                        aux->previous->next = aux->next;
                        aux->next->previous = aux->previous;
                    }
                    lst->numPersons = lst->numPersons - 1;
                    free(aux);
                    break;
                }
                aux = aux->next;
            }
        }
    }
    result = 1;
    return &result;
}

