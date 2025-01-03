from satgl.data.datasets.cnf_datasets import(
    SatistifiabilityDataset,
    MaxSATDataset,
    UnSATCoreDataset
)
from satgl.data.dataloaders.cnf_dataloaders import(
    SatistifiabilityDataLoader,
    MaxSATDataLoader,
    UnsatCoreDataLoader
)
from satgl.wrappers.data_wrappers.base_data_wrapper import DataWrapper


class CNFDataWrapper(DataWrapper):
    def __init__(self, root_dir, task, graph_type, log_file=False, batch_size=8) -> None:
        self.task = task
        self.batch_size = batch_size
        self.graph_type = graph_type
        print(self.task, self.batch_size, self.graph_type)
        super().__init__(root_dir, log_file)
    
    def get_dataset(self, dataset_path: str, label_path: str):
        if self.task == "satisfiability":
            return SatistifiabilityDataset(dataset_path, label_path, self.graph_type)
        elif self.task == "maxsat":
            return MaxSATDataset(dataset_path, label_path, self.graph_type)
        elif self.task == "unsat_core":
            return UnSATCoreDataset(dataset_path, label_path, self.graph_type)
        else:
            raise ValueError("Invalid task.")
    
    def get_dataloader(self, dataset: object, shuffle: bool = False):
        batch_size = self.batch_size
        # pair wise batching for satisfiability task
        if self.task == "satisfiability":
            batch_size = batch_size // 2
        
        if self.task == "satisfiability":
            return SatistifiabilityDataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
        elif self.task == "maxsat":
            return MaxSATDataLoader( dataset, batch_size=batch_size, shuffle=shuffle)
        elif self.task == "unsat_core":
            return UnsatCoreDataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
        else:
            raise ValueError("Invalid task.")