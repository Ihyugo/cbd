sum = 0.0
total = 0.0
for i in 0..100000000 do
	sum=2*i+1.0
	if i%2 == 0
		total += 1/sum
	else
		total -= 1/sum

	end
end
puts(4*total)
