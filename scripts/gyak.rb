#!/usr/bin/ruby -w

begin
 f = File.new(ARGV[0], "r")
rescue TypeError
 puts "ErrorCode: 1"
rescue Errno::ENOENT
   puts "ErrorCode: 1"   
end
k=File.new("ossz.txt", "w")

jegyek=Array.new
jegy=''
f.each_line do |line| 
 sor = line.split(' ')
 if line.length < 15
  sor.each do |alement|
   if alement.include? "-"
    alement.to_i
    jegy=alement.to_i
   end
  
  end
puts jegy
 else
  eredmeny=0
  nleadott=0
  leadott=5
  atmenet=0
  azon=''
   sor.each do |element|
     if element.include? ".ELTE"
      azon=element
     end
     if element.include? ","
      szam=element.delete(',').to_i
      eredmeny+=szam
     end 
     if element=='-' or element=='-,'
      nleadott+=1
     end
     atmenet=element.to_i
   end
  leadott=leadott-nleadott
  eredmeny+=atmenet
  jegy=0
  k.print(azon,"\t",eredmeny,"\t","(",leadott," feladat)")
 end

 
end
k.close

