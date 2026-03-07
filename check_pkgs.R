pkg_check <- require("MCPanel", quietly=TRUE)
cat("MCPanel available:", pkg_check, "\n")
if (!pkg_check) {
  cat("Trying to install MCPanel...\n")
  install.packages("MCPanel", repos="https://cran.r-project.org")
  cat("MCPanel after install:", require("MCPanel", quietly=TRUE), "\n")
}
cat("glmnet available:", require("glmnet", quietly=TRUE), "\n")
cat("softImpute available:", require("softImpute", quietly=TRUE), "\n")
