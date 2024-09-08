#ipa_data <- read.csv('ipa_collection.csv')
library(tidyverse)

#Important: Sort data
occur <- table(ipa_data$Name)
occur = sort(occur, TRUE)

# Creating unique dataframe for graphing
occurances <- data.frame(name = unique(ipa_data$Name))

occurances$frequency <- 0
occurances

# Assigning frequency values (How often phoneme occurs in data)
for(i in 1:length(occurances$name)) {
  occurances[i, 2] <- sum(ipa_data$Name == occurances[i,1])
}

# Sort data frame from lowest occurrences to highest
occurances <- arrange(occurances, occurances$frequency)

# Create data frame for specific amount of phonemes
top <- tail(occurances, 15)
top$frequency <- as.numeric(top$frequency)

# Add symbols for the phonemes to the dataset
top$symbol = ''
for(i in 1:length(top$name)) {
  top[i, 3] <- unique(ipa_data$Symbol[ipa_data$Name == top$name[i]])[1]
}

# "others" column
not_top_freq <- sum(head(occurances$frequency, nrow(occurances) - 5))
top[nrow(top)+1,] <- c("others", not_top_freq, '')

# Pie Chart
symbol_pos = c(0, 75, 210, 350, 475, 620)
ggplot(top, aes(x='', y=as.numeric(frequency), fill=name)) + 
  geom_bar(stat='identity', width=1, color='white') + 
  coord_polar('y', start=0) + 
  theme_void() + 
  labs(title="Top 5 Most Common Phonemes", caption="Using Data from Wikipedia IPA Pages") +
  geom_text(aes(y=symbol_pos, label = symbol), color='black', size=3)

# Bar Graph
ggplot(top, aes(x=reorder(symbol, -frequency), y=frequency, fill=name)) + 
  geom_bar(stat='identity') + 
  labs(x="Phoneme", y="Frequency", title="15 Commonest Phonemes", caption="Data from Wikipedia IPA Pages")
