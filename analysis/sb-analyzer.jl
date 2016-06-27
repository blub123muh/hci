#!/usr/bin/env julia
using DataFrames, DataArrays, HypothesisTests, Distributions
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
for field in [:Pid, :Tid]
  # Assert that all the Pid, Jid, groups have the same sizes
  chk = length(unique([size(subdf,1) for subdf in groupby(df, field)])) == 1
  println(field,": ", chk) 
end
burger_df = df[df[:navigation] .== "burger", :]
swipe_df = df[df[:navigation] .== "swipe", :]

burger = burger_df[:time_ms]
burger_mean, burger_std = mean_and_std(burger)
burger_isnorm_pval = pvalue(ExactOneSampleKSTest(burger, Normal(burger_mean, burger_std)))
burger_isnorm = burger_isnorm_pval < 0.05
println("Check Burger for normal distribution: $burger_isnorm [$burger_isnorm_pval]")
for swipe_task_df in groupby(swipe_df, :Tid)
  tid = swipe_task_df[1,:Tid]
  println("Swipe $tid against Burger")
  swipe_task = swipe_task_df[:time_ms]
  swipe_task_isnorm_pval = pvalue(ExactOneSampleKSTest(swipe_task, Normal(mean(swipe_task),std(swipe_task))))
  swipe_task_isnorm = swipe_task_isnorm_pval < 0.05
  println("Check Swipe Task $tid for normal distribution: $swipe_task_isnorm [$swipe_task_isnorm_pval]")
  if burger_isnorm && swipe_task_isnorm
    pval = pvalue(UnequalVarianceTTest(swipe_task, burger))
    println("  pvalue: $pval [Welch's T-Test]")
  else
    pval = pvalue(MannWhitneyUTest(swipe_task, burger))
    println("  pvalue: $pval [WMW U-Test]")
  end
end
