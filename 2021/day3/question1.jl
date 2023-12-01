include("input.jl")

input = split(input, "\n")

gamma = ""
epsilon = ""

for bit in 1:length(input[1])
    num0 = 0
    num1 = 0
    for byte in input
        if byte[bit] == '1'
            num1+=1
        else
            num0+=1
        end
    end
    global gamma *= string(Int(num0>num1))
    global epsilon *= string(Int(num0<num1))

end

println(parse(Int,gamma,base=2)*parse(Int,epsilon,base=2))
