library(dplyr)

inputs <- read.table(
  "Inputs/Input day 1",
  header = FALSE,
  col.names = c("var1", "var2")
)

solutions <- inputs %>%
  mutate(across(c(var1, var2),
                sort)) %>%
  left_join({.} %>% count(var2, name = "var2_count"),
            by = c("var1" = "var2")) %>%
  summarise(diff = sum(abs(var1 - var2)),
            sim = sum(var1 * var2_count, na.rm = TRUE))
  
