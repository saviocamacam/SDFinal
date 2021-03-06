/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include "llist.h"

bool_t
xdr_person (XDR *xdrs, person *objp)
{
	register int32_t *buf;

	 if (!xdr_string (xdrs, &objp->name, ~0))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->numTelefone, ~0))
		 return FALSE;
	 if (!xdr_pointer (xdrs, (char **)&objp->previous, sizeof (person), (xdrproc_t) xdr_person))
		 return FALSE;
	 if (!xdr_pointer (xdrs, (char **)&objp->next, sizeof (person), (xdrproc_t) xdr_person))
		 return FALSE;
	return TRUE;
}

bool_t
xdr_list (XDR *xdrs, list *objp)
{
	register int32_t *buf;

	 if (!xdr_pointer (xdrs, (char **)&objp->first, sizeof (person), (xdrproc_t) xdr_person))
		 return FALSE;
	 if (!xdr_pointer (xdrs, (char **)&objp->last, sizeof (person), (xdrproc_t) xdr_person))
		 return FALSE;
	 if (!xdr_int (xdrs, &objp->numPersons))
		 return FALSE;
	return TRUE;
}
