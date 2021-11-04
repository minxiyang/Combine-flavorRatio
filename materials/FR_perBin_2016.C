void FR_perBin_2016()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Nov  4 03:43:56 2021) by ROOT version 6.12/07
   TCanvas *c = new TCanvas("c", "c",0,0,800,800);
   c->SetHighLightColor(2);
   c->Range(-691.8919,-0.25,3767.568,2.25);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetGridx();
   c->SetGridy();
   c->SetLeftMargin(0.2);
   c->SetRightMargin(0.06);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   TH1D *__1 = new TH1D("__1","",1,200,3500);
   __1->SetMinimum(0);
   __1->SetMaximum(2);
   __1->SetEntries(1);
   __1->SetStats(0);
   __1->SetLineColor(0);
   __1->SetLineWidth(0);
   __1->GetXaxis()->SetTitle("m_{#mu#mu} [GeV]");
   __1->GetXaxis()->SetLabelFont(42);
   __1->GetXaxis()->SetLabelSize(0.035);
   __1->GetXaxis()->SetTitleSize(0.035);
   __1->GetXaxis()->SetTitleFont(42);
   __1->GetYaxis()->SetTitle("Flavor Ratio (R)");
   __1->GetYaxis()->SetLabelFont(42);
   __1->GetYaxis()->SetLabelSize(0.035);
   __1->GetYaxis()->SetTitleSize(0.035);
   __1->GetYaxis()->SetTitleOffset(0);
   __1->GetYaxis()->SetTitleFont(42);
   __1->GetZaxis()->SetLabelFont(42);
   __1->GetZaxis()->SetLabelSize(0.035);
   __1->GetZaxis()->SetTitleSize(0.035);
   __1->GetZaxis()->SetTitleFont(42);
   __1->Draw("");
   
   Double_t Graph0_fx3001[9] = {
   250,
   350,
   450,
   595,
   795,
   1075,
   1430,
   1805,
   2750};
   Double_t Graph0_fy3001[9] = {
   0.9698842,
   0.9885061,
   0.9657459,
   0.9745076,
   0.8401098,
   0.9571098,
   1.079528,
   0.06129137,
   0.4428428};
   Double_t Graph0_felx3001[9] = {
   50,
   50,
   50,
   95,
   105,
   175,
   180,
   195,
   750};
   Double_t Graph0_fely3001[9] = {
   0.006393313,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph0_fehx3001[9] = {
   50,
   50,
   50,
   95,
   105,
   175,
   180,
   195,
   750};
   Double_t Graph0_fehy3001[9] = {
   0.006412923,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(9,Graph0_fx3001,Graph0_fy3001,Graph0_felx3001,Graph0_fehx3001,Graph0_fely3001,Graph0_fehy3001);
   grae->SetName("Graph0");
   grae->SetTitle("Graph");
   grae->SetFillStyle(1000);
   grae->SetLineWidth(2);
   
   TH1F *Graph_Graph3001 = new TH1F("Graph_Graph3001","Graph",100,0,3830);
   Graph_Graph3001->SetMinimum(0.05516223);
   Graph_Graph3001->SetMaximum(1.181352);
   Graph_Graph3001->SetDirectory(0);
   Graph_Graph3001->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph3001->SetLineColor(ci);
   Graph_Graph3001->GetXaxis()->SetLabelFont(42);
   Graph_Graph3001->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3001->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3001->GetXaxis()->SetTitleFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3001->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3001->GetYaxis()->SetTitleOffset(0);
   Graph_Graph3001->GetYaxis()->SetTitleFont(42);
   Graph_Graph3001->GetZaxis()->SetLabelFont(42);
   Graph_Graph3001->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3001->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3001);
   
   grae->Draw("p");
   
   TLegend *leg = new TLegend(0.6,0.7,0.9,0.87,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetLineColor(0);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph0","Observed Flavor Ratio","l");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   TH1D *_copy__2 = new TH1D("_copy__2","",1,200,3500);
   _copy__2->SetMinimum(0);
   _copy__2->SetMaximum(2);
   _copy__2->SetEntries(1);
   _copy__2->SetDirectory(0);
   _copy__2->SetStats(0);
   _copy__2->SetLineColor(0);
   _copy__2->SetLineWidth(0);
   _copy__2->GetXaxis()->SetTitle("m_{#mu#mu} [GeV]");
   _copy__2->GetXaxis()->SetLabelFont(42);
   _copy__2->GetXaxis()->SetLabelSize(0.035);
   _copy__2->GetXaxis()->SetTitleSize(0.035);
   _copy__2->GetXaxis()->SetTitleFont(42);
   _copy__2->GetYaxis()->SetTitle("Flavor Ratio (R)");
   _copy__2->GetYaxis()->SetLabelFont(42);
   _copy__2->GetYaxis()->SetLabelSize(0.035);
   _copy__2->GetYaxis()->SetTitleSize(0.035);
   _copy__2->GetYaxis()->SetTitleOffset(0);
   _copy__2->GetYaxis()->SetTitleFont(42);
   _copy__2->GetZaxis()->SetLabelFont(42);
   _copy__2->GetZaxis()->SetLabelSize(0.035);
   _copy__2->GetZaxis()->SetTitleSize(0.035);
   _copy__2->GetZaxis()->SetTitleFont(42);
   _copy__2->Draw("sameaxis");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
