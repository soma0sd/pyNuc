# Data Files for DB Analysis

 * `ensdf_nucid_zz.csv`: trans integer number for Atomic Symbol in ENSDF NUCID.
   * column 1: ENSDF atomic symbol
   * column 2: atomic number
 * `ensdf_decay_delta`: decay product data of each decay modes. decay mode symbol is appended '%' character. ex) `%B-N`: neutron emission beta minus decay. mass number: -1, atomic number: +1
   * column 1: ENSDF decay mode. (appended '%' character)
   * column 2: delta Z (atomic number)
   * column 3: delta A (mass number)