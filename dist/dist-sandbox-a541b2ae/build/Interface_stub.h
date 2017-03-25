#include "HsFFI.h"
#ifdef __cplusplus
extern "C" {
#endif
extern void __free(HsPtr a1);
extern HsPtr laplace__info(void);
extern HsPtr laplace__export(HsPtr a1);
extern HsPtr schrodinger__info(void);
extern HsPtr schrodinger__export(HsPtr a1, HsPtr a2, HsDouble a3);
extern HsPtr solve__info(void);
extern HsPtr solve__export(HsPtr a1, HsPtr a2, HsDouble a3, HsInt32 a4);
#ifdef __cplusplus
}
#endif

