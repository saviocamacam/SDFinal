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

/* print out a list, returning the number of items printed */
int *add_person_1_svc(person *prs, struct svc_req *req)
{
    person * ptr;
    ptr = prs;

    if(lst == NULL) {
        createList();
        if(lst == NULL)
            printf("Deu merda ao criar a lista. Por que? Nao sei\n");
    }
    
    person * aux = lst->first;
    if(aux == NULL){
        lst->first = ptr;
        lst->last = ptr;
        lst->numPersons = lst->numPersons + 1;
    }
    else {
        while(aux != NULL) {
            printf("nome: %s\n", aux->name);
            printf("telefone: %s\n", aux->numTelefone);
            aux = aux->next;
        }
        ptr->previous = lst->last;
        lst->last->next = ptr;
        lst->last = ptr;
        lst->numPersons = lst->numPersons + 1;
        printf("nome: %s\n", lst->last->name);
        printf("telefone: %s\n", lst->last->numTelefone);
    }
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

