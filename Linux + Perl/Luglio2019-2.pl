#!/usr/bin/perl
$opzione=shift or die "opzione";
$file=shift or die"file";

if($opzione eq "-s")
{
    open(my $fh,">",$file);
    @output=qx(lshw);
    for(my $i=0;$i<@output;$i++)
    {
        print $fh "@output[$i]";
        print "@output[$i]";
    }
    close $fh;
}
elsif($opzione eq "-b")
{
    open(my $fh,"<",$file)or $!;
    # Conta e stampa in ordine decrescente il numero dei dispositivi forniti per ogni
    # vendor (a parità di numero di dispositivi, è necessario stampare il vendor in
    # ordine alfabetico);
    %array;
    %description;
    while(<$fh>)
    {
        chomp;
        if($_=~m/vendor:\s(.+)/)
        {
            $array{$1}+=1;
            #$description{$1}=$1;
        }
    }

    foreach $values(sort {$array{$b}<=>$array{$a} or {$a cmp $b}} keys %array )#or {$a cmp $b}
    {
        print "$values --> $array{$values}\n"
    }

    # while(my($keys, $values)=each %array)
    # {
    #     print "$keys --> $values\n";
    # }

    close $fh;
}