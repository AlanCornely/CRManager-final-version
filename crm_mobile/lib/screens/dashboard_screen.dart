import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/inventory_provider.dart';
import '../providers/sales_provider.dart';
import '../providers/auth_provider.dart';
import '../theme/app_theme.dart';
import 'inventory_screen.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  @override
  void initState() {
    super.initState();
    // Fetch data on init
    WidgetsBinding.instance.addPostFrameCallback((_) {
      context.read<InventoryProvider>().fetchProducts();
      // Clients mock fetch or real if implemented
      context.read<InventoryProvider>().fetchClients();
    });
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final inventory = context.watch<InventoryProvider>();
    final sales = context.watch<SalesProvider>();
    final auth = context.read<AuthProvider>();

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('CRManager', style: TextStyle(fontWeight: FontWeight.bold)),
            Text('Visão geral do negócio', style: theme.textTheme.bodySmall),
          ],
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
               auth.logout();
               // Navigator pop is handled by main wrapper
            },
          )
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              decoration: BoxDecoration(color: theme.colorScheme.primary),
              child: const Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                   Icon(Icons.inventory_2, size: 48, color: Colors.white),
                   SizedBox(height: 8),
                   Text('CRManager', style: TextStyle(color: Colors.white, fontSize: 24)),
                ],
              ),
            ),
            ListTile(
              leading: const Icon(Icons.dashboard),
              title: const Text('Dashboard'),
              selected: true,
              onTap: () => Navigator.pop(context),
            ),
            ListTile(
              leading: const Icon(Icons.inventory),
              title: const Text('Estoque'),
              onTap: () {
                Navigator.pop(context); // Close drawer
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const InventoryScreen()),
                );
              },
            ),
            ListTile(
              leading: const Icon(Icons.shopping_cart),
              title: const Text('Vendas (PDV)'),
              onTap: () {
                // Navigate to Sales Screen (TODO)
                 Navigator.pop(context);
              },
            ),
            // ... other items
          ],
        ),
      ),
      body: inventory.isLoading
          ? const Center(child: CircularProgressIndicator())
          : RefreshIndicator(
              onRefresh: () => inventory.fetchProducts(),
              child: SingleChildScrollView(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Stats Grid
                    GridView.count(
                      crossAxisCount: MediaQuery.of(context).size.width > 600 ? 4 : 2,
                      crossAxisSpacing: 16,
                      mainAxisSpacing: 16,
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      children: [
                        _buildStatCard(
                          context,
                          'Total de Itens',
                          '${inventory.totalItems}',
                          Icons.inventory_2_outlined,
                          AppTheme.primaryColor,
                        ),
                        _buildStatCard(
                          context,
                          'Valor em Estoque',
                          'R\$ ${(inventory.totalStockValue).toStringAsFixed(2)}',
                          Icons.attach_money,
                          AppTheme.secondaryColor,
                        ),
                        _buildStatCard(
                          context,
                          'Vendas Hoje',
                          '${sales.salesTodayCount}', // Mock
                          Icons.shopping_bag_outlined,
                          Colors.teal, // accent
                        ),
                        _buildStatCard(
                          context,
                          'Baixo Estoque',
                          '${inventory.lowStockCount}',
                          Icons.warning_amber_rounded,
                          Colors.red,
                        ),
                      ],
                    ),
                    
                    const SizedBox(height: 24),
                    const Text('Vendas Recentes', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                    const SizedBox(height: 16),
                    
                    // Recent Sales List
                    Card(
                      child: sales.sales.isEmpty 
                        ? const Padding(
                            padding: EdgeInsets.all(32.0),
                            child: Center(child: Text('Nenhuma venda registrada ainda.')),
                          )
                        : ListView.separated(
                            shrinkWrap: true,
                            physics: const NeverScrollableScrollPhysics(),
                            itemCount: sales.recentSales.length,
                            separatorBuilder: (_, __) => const Divider(),
                            itemBuilder: (context, index) {
                              final sale = sales.recentSales[index];
                              return ListTile(
                                leading: CircleAvatar(child: Text(sale.clientName.substring(0,1).toUpperCase())),
                                title: Text(sale.itemName),
                                subtitle: Text('${sale.clientName} • ${sale.date}'),
                                trailing: Text('R\$ ${sale.total.toStringAsFixed(2)}', style: const TextStyle(fontWeight: FontWeight.bold, color: Colors.green)),
                              );
                            },
                          ),
                    ),
                  ],
                ),
              ),
            ),
    );
  }

  Widget _buildStatCard(BuildContext context, String title, String value, IconData icon, Color color) {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Icon(icon, color: color),
              ],
            ),
            const Spacer(),
            Text(title, style: const TextStyle(fontSize: 12, color: Colors.grey)),
            const SizedBox(height: 4),
            Text(value, style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: color)),
          ],
        ),
      ),
    );
  }
}
