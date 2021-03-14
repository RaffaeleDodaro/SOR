#!/usr/bin/perl
$opzione=shift or die $!;
$username;
if($opzione=~m/-user/)
{
    $username=shift or die $!;
}
$nome_file=shift or die $!;
open($fh,"<",$nome_file);
if($opzione=~m/-ip/)
{
    %ip_tentativi;
    while(<$fh>)
    {
        if($_ =~ m/Failed password for invalid user .+\s(\d+\.\d+\.\d+.\d+)/)
        {
            # (\d+\.\d+\.\d+.\d+)
            $ip_tentativi{$1}+=1;
        }
        chomp;
    }
    
    foreach $tentativi(sort{$ip_tentativi{$b}<=>$ip_tentativi{$a}} keys %ip_tentativi)
    {
        print "$tentativi --> $ip_tentativi{$tentativi}\n";
    }
}
elsif($opzione=~m/-user/)
{
    $accessi=0;
    @date;
    while(<$fh>)
    {
        chomp;
        if($_ =~ m/(\w+\s+\d+).+Failed password for invalid user ($username)/)
        {
            $accessi+=1;
            push(@date, $1);
        }        
    }
    open($fh2,">>","nuovoFile.txt");

    print $fh2 "$username - $accessi\n";
    for($i=0;$i<@date;$i++)
    {
        print $fh2 @date[$i]."\n";
    }

    close $fh2;
}
close $fh;