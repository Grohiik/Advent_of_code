include("input.jl")

o2input = split(input, "\n")
c2input = split(input, "\n")


for bit in 1:length(o2input[1])
    num0 = 0
    num1 = 0
    for byte in o2input
        if byte[bit] == '1'
            num1+=1
        else
            num0+=1
        end
    end
    thing = string(Int(num1>=num0))
    if length(o2input) == 1
        break
    end
    for byte in length(o2input):-1:1
        if string(o2input[byte][bit]) != thing
            deleteat!(o2input, byte)
        end
    end
end


for bit in 1:length(c2input[1])
    num0 = 0
    num1 = 0
    for byte in c2input
        if byte[bit] == '1'
            num1+=1
        else
            num0+=1
        end
    end
    thing = string(Int(num0>num1))
    if length(c2input) == 1
        break
    end
    for byte in length(c2input):-1:1
        if string(c2input[byte][bit]) != thing
            deleteat!(c2input, byte)
        end
    end
end

println(parse(Int,o2input[1],base=2)*parse(Int,c2input[1],base=2))