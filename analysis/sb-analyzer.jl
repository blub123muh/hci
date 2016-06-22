#!/usr/bin/env julia
using DataFrames
#= TODO: CLI =#
#= read table from csv =#
df = readtable("data-format.csv")
# Assert data is complete and unique per Pid
#= for subdf in groupby(df, :Pid) =#
#=   println("pid check", size(subdf,1)) =#
#= end =#

# Fancy one-line data validation for participants ID
# TODO this could be done for other Task IDs aswell
println("Validating dataset...")
for field in [:Pid, :Jid]
  chk = length(unique([size(subdf,1) for subdf in groupby(df, field)])) == 1
  println(field,": ", chk) 
end

# Group by Navigation Method
for nav_df in groupby(df, :navigation)
  println("Processing navigation method ", nav_df[1, :navigation], "...")
  for task_df in groupby(nav_df, :Tid)
    println("Task", task_df[1,:Tid])
    task_values = task_df[:time_ms]
    println(task_values)
    #= describe(task_df[:time_ms]) =# 
  end
end
