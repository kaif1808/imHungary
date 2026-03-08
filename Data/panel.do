clear
local file "/Users/kai/Documents/BSE/14E022_Macroeconomics_I/imHungary/Data/HU_labour_accounts.xlsx"

* 1. Describe once and capture all sheet info before any import
import excel using "`file'", describe
local n_sheets = r(N_worksheet)

forvalues i = 1/`n_sheets' {
    local sheet`i' "`r(worksheet_`i')'"
}

* 2. Use sheet 2 as the base (sheet 1 is Legend)
import excel using "`file'", sheet("`sheet2'") firstrow clear
gen sheetname = "`sheet2'"
save "all_sheets.dta", replace

* 3. Loop over remaining sheets 3..n and append into base
forvalues s = 3/`n_sheets' {
    import excel using "`file'", sheet("`sheet`s''") firstrow clear
    gen sheetname = "`sheet`s''"
    append using "all_sheets.dta"
    save "all_sheets.dta", replace
}

rename F  val1995
rename G  val1996
rename H  val1997
rename I  val1998
rename J  val1999
rename K  val2000
rename L  val2001
rename M  val2002
rename N  val2003
rename O  val2004
rename P  val2005
rename Q  val2006
rename R  val2007
rename S  val2008
rename T  val2009
rename U  val2010
rename V  val2011
rename W  val2012
rename X  val2013
rename Y  val2014
rename Z  val2015
rename AA val2016
rename AB val2017
rename AC val2018
rename AD val2019
rename AE val2020
rename AF val2021
rename code nace_r2_code
egen var = concat(sheetname education age gender)

reshape long val, i(nace_r2_code var) j(year)

drop id sheetname id_str
drop education age gender
isid year nace_r2_code var

reshape wide val, i(year nace_r2_code) j(var) string

