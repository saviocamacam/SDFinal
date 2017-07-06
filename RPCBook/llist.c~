/*
  llist printer RPC client
  by Jeff Bezanson
*/

#include "llist.h"

person *mk_person(char *name, char *num)
{
    person *prs;

    prs = (person*)malloc(sizeof(person));
    if (prs == NULL)
        return NULL;
    prs->name = name;
    prs->numTelefone = num;
    prs->next = NULL;
    prs->previous = NULL;
    return prs;
}

int main(int argc, char *argv[])
{
    CLIENT *cl;
    list * lst;

    int option = -1;
    char name[30];
    char num[30];

    person * prs;
    int * result;

    cl = clnt_create(argv[1], MANAGER, MANAGER_V1, "tcp");
    if (cl == NULL) {
        printf("error: could not connect to server.\n");
        return 1;
    }

    do {
        printf("(1) ADICIONAR CONTATO\n");
        printf("(2) REMOVER CONTATO\n");
        printf("(3) LISTAR CONTATOS\n");
        printf("(4) SAIR\n");

        option = scanf("%d", &option);

        switch(option) {
            case 1:
                printf("ADICIONAR CONTATO\n");
                printf("Informe o nome: ");
                scanf("%[^\n]s", name);
                printf("\nInforme o numero: ");
                scanf("%[^\n]s", num);
                prs = mk_person(name, num);

                if(prs == NULL)
                    printf("Erro ao criar %s\n", name);

                result = add_person_1(prs, cl);
                if (result == NULL) {
                    printf("error: RPC failed!\n");
                    return 1;
                }
                printf("Contato adicionado com sucesso!\n");
                break;
            case 2:
                printf("REMOVER CONTATO\n");
                printf("Informe o nome: ");
                scanf("%[^\n]s", name);
                printf("\nInforme o numero: ");
                scanf("%[^\n]s", num);
                prs = mk_person(name, num);

                result = remove_person_1(prs, cl);
                if (result == NULL) {
                    printf("error: RPC failed!\n");
                    return 1;
                }
                if(*result == 1)
                    printf("Contato adicionado com sucesso!\n");
                else if(*result == 0)
                    printf("Contato nao localizado!\n");
                break;
            case 3:
                printf("Solicitando lista de contados no servidor: \n");
                /*int *value = (int*)1;
                lst = get_list_1(value,cl);
                if(lst == NULL) {
                    printf("Lista inexistente!\n");
                }
                else {
                    person * aux = lst->first;
                    int indice = 0;
                    while(aux != NULL) {
                        printf("Person(%d)\n", indice++);
                        printf("nome: %s\n", aux->name);
                        printf("numero: %s\n", aux->numTelefone);
                        aux = aux->next;
                    }
                }*/
                break;
            default:
                break;
        }
    } while(option != 4);

    return 0;
}
