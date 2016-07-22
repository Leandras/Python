#!/usr/bin/ruby -w
#Script nyelvek Beadandó 5
#Lévai András
#AGY276
#levaiandrass@gmail.com

begin
 f = File.new(ARGV[0], "r")
rescue TypeError
 puts "ErrorCode: 1"
rescue Errno::ENOENT
   puts "ErrorCode: 1"   
end
k=File.new("zh_ossz2.txt", "w")

jegyek=Array.new
segit=0
f.each_line do |line| 
 sor = line.split(' ')
 if line.length < 15
  segit=1
  sor.each do |alement|
   if alement.include? "-"
    jegyek.push alement.to_i   
   end
  end
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
  i=0
  if segit == 1
   megadom=0
   while i < 5 do
    if eredmeny < jegyek[i]
     megadom=i
     i=5
    else
     megadom=5
    end
    i+=1
   end
   k.print(azon,"\t",eredmeny,"\t","(",leadott," feladat)",", jegy: ",megadom,"\n")
  else
   k.print(azon,"\t",eredmeny,"\t","(",leadott," feladat)","\n")
  end
 end
end
k.close

