#ipa_data <- read.csv('ipa_collection.csv')

#Important: Sort data
occur <- table(ipa_data$Name)
occur = sort(occur, TRUE)

# Top 10 most common phonemes
print(occur[1:10])

# Pie Chart
not_top = sum(occur[6:length(occur)])
chart = c(occur[1:5], not_top)
pie(chart, main = "Top 5 Most Common Phonemes")

# Bar Graph
plot(occur, ylab = "Occurances in a language", xlab="Phoneme")
