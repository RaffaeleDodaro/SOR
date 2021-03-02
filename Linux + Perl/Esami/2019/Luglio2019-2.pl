#!/usr/bin/perl
$opzione=shift or die "opzione";
$file=shift or die"file";

if($opzione eq "-s")
{
    open(my $fh,">",$file)or die $!;
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
    open(my $fh,"<",$file)or die $!;
    # Conta e stampa in ordine decrescente il numero dei dispositivi forniti per ogni
    # vendor (a parità di numero di dispositivi, è necessario stampare il vendor in
    # ordine alfabetico);
    %array;
    %description;
    while(<$fh>)
    {
        chomp;
        print $_;
        if($_=~m/description: (.+)\n.+\n\s+vendor: (.+)/)
        {
            print "ciao";
            $array{$2}+=1;
            $description{$2}="description: $1\n $description{$2}";
        }
    }
    foreach $values(sort {$array{$b}<=>$array{$a} or {$a cmp $b}} keys %array )
    {
        print "$values --> $array{$values}\n"
    }

    foreach $values(sort {{$a cmp $b}} keys %description )
    {
        print "$values --> $description{$values}\n"
    }

    # while(my($keys, $values)=each %array)
    # {
    #     print "$keys --> $values\n";
    # }

    close $fh;
}