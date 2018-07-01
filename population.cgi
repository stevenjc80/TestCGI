#!/usr/bin/perl -wT
# This cgi script responds with country information. This was used to provide
# web-based input for CS2 Java programming tests.
# Written by Steven Castellucci, Copyright 2015.

use CGI qw(:all);
use CGI::Carp qw(fatalsToBrowser);
use strict;

my $country = (defined param("country")) ? param("country") : "";
print "Content-type: text/html\n\n";

if($country eq "Canada")
{
	print "Capital:Ottawa\n";
	print "Population:35985751\n";
	print "Area (sq km):9984670\n";
	print "Languages:English, French\n";
	print "Currency:Dollar\n";
}
elsif ($country eq "China")
{
	print "Area (sq km):9326411\n";
	print "Population:1355692576\n";
	print "Languages:Mandarin\n";
	print "Capital:Beijing\n";
	print "Currency:Yuan\n";
}
elsif ($country eq "India")
{
	print "Population:1236344631\n";
	print "Capital:New Delhi\n";
	print "Area (sq km):2973190\n";
	print "Languages:Hindi, English\n";
	print "Currency:Rupee\n";
}
elsif ($country eq "United States")
{
	print "Area (sq km):9166601\n";
	print "Currency:Dollar\n";
	print "Capital:Washington, DC\n";
	print "Languages:English, Spanish\n";
	print "Population:318892103\n";
}
elsif ($country eq "Indonesia")
{
	print "Capital:Jakarta\n";
	print "Area (sq km):1811831\n";
	print "Currency:Rupiah\n";
	print "Population:253609643\n";
	print "Languages:Indonesian\n";
}
elsif ($country eq "Brazil")
{
	print "Population:205716890\n";
	print "Languages:Portuguese\n";
	print "Currency:Real\n";
	print "Area (sq km):8456511n";
	print "Capital:Brasilia\n";
}
else
{
	print "???\n";
}
