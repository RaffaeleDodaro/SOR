#!/usr/bin/perl
$opzione=shift or die $!;
$username;
if($opzione=~m/-user/)
{
    $username=shift or die $!;
    print "$username\n";
}
$nome_file=shift or die $!;

if($opzione=~m/-ip/)
{
    open($fh,"<",$nome_file);
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
    close $fh;
    foreach $tentativi(sort{$ip_tentativi{$b}<=>$ip_tentativi{$a}} keys %ip_tentativi)
    {
        print "$tentativi --> $ip_tentativi{$tentativi}\n";
    }
}
elsif($opzione=~m/-user/)
{
    open($fh,"<",$nome_file);
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
    close $fh;
    open($fh,">>","nuovoFile.txt");

    print $fh "$username - $accessi\n";
    for($i=0;$i<@date;$i++)
    {
        print $fh @date[$i]."\n";
    }

    close $fh;
}